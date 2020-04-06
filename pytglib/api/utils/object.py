from collections import OrderedDict
from json import JSONEncoder, dumps


class Object:
    all = {}

    @staticmethod
    def read(q: dict, *args):
        if q is None:
            return None
        if isinstance(q, Object):
            return q
        if not isinstance(q, dict):
            return q
        for key, value in q.items():
            if isinstance(value, dict) and value.get("@type", False):
                q[key] = Object.all[value["@type"]].read(value)
        return Object.all[q["@type"]].read(q, *args)

    def __str__(self) -> str:
        return dumps(self, cls=Encoder, indent=4)

    def __bytes__(self):
        return dumps(self, cls=Encoder).encode('utf-8')

    def __bool__(self) -> bool:
        return True

    def __eq__(self, other) -> bool:
        return self.__dict__ == other.__dict__

    def __len__(self) -> int:
        return len(self.__str__())

    def __call__(self):
        pass

    def __getitem__(self, item):
        return getattr(self, item)


class Encoder(JSONEncoder):
    def default(self, o: Object):
        content = o.__dict__
        o = getattr(o, "ID", "")
        r = OrderedDict([("@type", o)] + [i for i in content.items()])
        if r.get("extra"):
            r["@extra"] = r.pop("extra")
        return r
