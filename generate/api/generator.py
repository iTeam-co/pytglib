import os
import re
import shutil
import urllib.request

HOME = "generate/api"
DESTINATION = "pytglib/api"
SECTION_RE = re.compile("---(\w+)---")
COMBINATOR_RE = re.compile(r'^(\w+)\s(?:.*)=\s(\w+);$', re.MULTILINE)
ARGS_RE = re.compile("(\w+):([\w<>]+)")
DOCS_RE = re.compile(r"^//@")
DOCS_RE1 = re.compile(r"^//-")
DOCS_RE_2 = re.compile(r"^//@description")
DOCS_RE_3 = re.compile(r"^//@class")

core_types = {
    'int': 'int', 'int32': 'int', 'int53': 'int', 'int64': 'int', 'long': 'int', 'double': 'float',
    'string': 'str',
    'bytes': 'bytes',
    'Bool': 'bool'
}


def upper_first(s: str):
    return s[:1].upper() + s[1:]


def lower_first(s: str):
    return s[:1].lower() + s[1:]


def snek(s: str):
    # https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case
    s = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', s)
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', s).lower()


class Combinator:
    def __init__(self, section: str, name: str, doc: list, args: list, return_type: str):
        self.section = section
        self.name = name
        self.doc = doc
        self.args = args
        self.return_type = return_type


class ClassCombinator:
    def __init__(self, name, doc):
        self.section = "types"
        self.name = name
        self.doc = doc
        self.sub_classes = set()


def start():
    shutil.rmtree("{}/types/".format(DESTINATION), ignore_errors=True)
    shutil.rmtree("{}/functions/".format(DESTINATION), ignore_errors=True)

    try:
        scheme = urllib.request.urlopen("https://raw.githubusercontent.com/tdlib/td/master/td/generate/scheme/td_api.tl").read().decode('utf-8')
    except:
        with open('{}/source/td_api.tl'.format(HOME), encoding='utf-8') as f:
            scheme = f.read()

    with open("{}/template/class.txt".format(HOME), encoding="utf-8") as f:
        template = f.read()

    notice = ""

    section = "types"
    class_name = ""
    combinators = []
    class_combinators = {}
    descriptions = []
    scheme_data = scheme.splitlines()
    return_types = set()
    for line in scheme_data[14:]:
        s = SECTION_RE.match(line)
        if s:
            section = "functions"
            continue

        document = DOCS_RE.match(line)
        if document:

            cls = DOCS_RE_3.match(line)
            if cls:
                class_name = line.split('@class ', 1)[1].split(' ', 1)[0]
                doc = line.split('@description ', 1)[1]
                class_combinators[class_name] = ClassCombinator(class_name, doc)
                continue

            start_doc = DOCS_RE_2.match(line)
            if start_doc:
                line = line.replace('description ', '', 1)

            line = line[3:]

            description = line.split('@')
            for des in description:
                descriptions.append(des)
                continue
        more_doc = DOCS_RE1.match(line)
        if more_doc:
            line = line[3:]
            more_description = line.split('@')
            if more_description:
                if descriptions:
                    descriptions[-1] += more_description[0]
                else:
                    class_combinators[class_name].doc += more_description[0]
                for d in more_description[1:]:
                    descriptions.append(d)
            else:
                if descriptions:
                    descriptions[-1] += line
                else:
                    class_combinators[class_name].doc += line

        combinator = COMBINATOR_RE.match(line)
        if combinator:
            name, return_type = combinator.groups()
            args = ARGS_RE.findall(line)
            combinators.append(
                Combinator(
                    section,
                    upper_first(name),
                    descriptions,
                    args,
                    return_type,
                )
            )

            if section == "types" and return_type in class_combinators:
                class_combinators[return_type].sub_classes.add(name)
            if section == "functions":
                return_types.add(return_type)
            descriptions = []
    for combinator in class_combinators.values():
        combinators.append(combinator)

    total = len(combinators)
    current = 0
    for c in combinators:
        print('Generating [{0:03}%] {name}'.format(
            round(current * 100 / total), name=c.name
        ), end='                                        \r', flush=True)
        current += 1

        path = "{}/{}".format(DESTINATION, c.section)
        os.makedirs(path, exist_ok=True)
        init = "{}/__init__.py".format(path)
        if not os.path.exists(init):
            with open(init, "w", encoding="utf-8") as f:
                f.write(notice)

        with open(init, "a", encoding="utf-8") as f:
            f.write("from .{} import {}\n".format(snek(c.name), c.name))

        extra, has_extra = (", extra=None", "self.extra = extra") if c.section == "functions" else ("", "")

        if isinstance(c, ClassCombinator):
            doc_args = str(c.doc) + "\n\n    No parameters required."
            imports = ""
            read_args = 'if q.get("@type"):\n            return Object.read(q)'
            arguments = ""
            fields = "pass"
            return_arguments = ""
            return_read = " or ".join(upper_first(r_name) for r_name in c.sub_classes)
        else:
            doc_args = []
            read_args = []
            fields = []
            imports = ""

            for i, arg in enumerate(c.args):
                arg_name, arg_type = arg

                if arg_type in core_types:
                    field_type = core_types[arg_type]
                    arg_type = "(:obj:`{}`)".format(core_types[arg_type])
                    arg_read = "q.get('{}')".format(arg_name)

                elif arg_type.startswith("vector"):
                    sub_type = arg_type.split("<", 1)[1][:-1]

                    if sub_type.startswith("vector"):
                        sub_type = sub_type.split("<", 1)[1][:-1]
                        if sub_type in core_types:
                            arg_type = "(List of List of :obj:`{}`)".format(core_types[sub_type])
                            field_type = "list of List of {}".format(core_types[sub_type])
                            arg_read = "q.get('{}')".format(arg_name)

                        else:
                            arg_type = "(List of List of :class:`telegram.api.types.{}`)".format(sub_type)
                            field_type = "list of list({})".format(sub_type)
                            arg_read = "[[{}.read(v) for v in i] for i in q.get('{}', [])]".format(
                                # upper_first(sub_type),
                                "Object",
                                arg_name
                            )
                            # imports += "from .{} import {}\n".format(snek(sub_type), upper_first(sub_type))
                    else:
                        if sub_type in core_types:
                            arg_type = "(List of :obj:`{}`)".format(core_types[sub_type])
                            field_type = "list of {}".format(core_types[sub_type])
                            arg_read = "q.get('{}')".format(arg_name)

                        else:
                            arg_type = "(List of :class:`telegram.api.types.{}`)".format(sub_type)
                            field_type = "list of {}".format(sub_type)
                            arg_read = "[{}.read(i) for i in q.get('{}', [])]".format(
                                # upperfirst(sub_type),
                                "Object",
                                arg_name
                            )
                            # imports += "from .{} import {}\n".format(snek(sub_type), upper_first(sub_type))

                else:
                    field_type = upper_first(arg_type)
                    arg_read = "{}.read(q.get('{}'))".format(
                        # field_type,
                        "Object",
                        arg_name
                    )
                    # imports += "from .{} import {}\n".format(snek(arg_type), field_type)
                    arg_type = "(:class:`telegram.api.types.{}`)".format(arg_type)

                doc_args.append(
                    "{} {}".format(
                        arg_name, arg_type,
                    )
                )

                fields.append(
                    "self.{0} = {0}  # {1}".format(arg_name, field_type)
                )

                read_args.append(
                    "{} = {}".format(
                        arg_name, arg_read,
                    )
                )

            if doc_args:
                doc_args = "Args:\n        " + "\n        ".join(
                    "{}:\n            {}".format(
                        doc_args[i],
                        "".join(
                            darg[1:] if darg.startswith(' ') else darg
                            for darg in c.doc[i + 1].split(' ', 1)[1].split('.'))
                    ) for i in range(len(doc_args)))
                read_args = "\n        ".join(read_args)
            else:
                doc_args = "No parameters required."
                read_args = ""

            doc_args = c.doc[0] + "\n\n    Attributes:\n        ID (:obj:`str`): ``{}``\n\n    ".format(
                c.name) + doc_args
            doc_args += "\n\n    Returns:\n        " + c.return_type
            doc_args += "\n\n    Raises:\n        :class:`telegram.Error`"

            arguments = ", " + ", ".join(
                [i[0] for i in c.args]
            ) if c.args else ""

            fields = "\n        ".join(
                fields
            ) if fields else "pass"

            return_arguments = ", ".join(
                [i[0] for i in c.args]
            ) if c.args else ""

            return_read = c.name

        with open("{}/{}/{}.py".format(DESTINATION, c.section, snek(c.name)), "w+", encoding="utf-8") as f:
            f.write(
                template.format(
                    notice=notice,
                    imports=imports,
                    extra=extra,
                    has_extra=has_extra,
                    docstring=doc_args,
                    class_name=c.name,
                    ID=lower_first(c.name),
                    arguments=arguments,
                    fields=fields,
                    return_read=return_read,
                    read=read_args,
                    return_arguments=return_arguments
                )
            )
    with open("{}/utils/all_types.py".format(DESTINATION), "w", encoding="utf-8") as f:

        f.write(notice + "\n\n")
        f.write("all_types = {")

        for c in combinators:
            if c.section == "types":
                f.write("\n    \"{0}\": \"{1}\",".format(c.name, snek(c.name)))
        f.write("\n}\n")


if '__main__' == __name__:
    HOME = "."
    DESTINATION = "../../pytglib/api"
    start()
