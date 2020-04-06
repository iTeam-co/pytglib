

from ..utils import Object


class ParseTextEntities(Object):
    """
    Parses Bold, Italic, Underline, Strikethrough, Code, Pre, PreCode, TextUrl and MentionName entities contained in the text. This is an offline method. Can be called before authorization. Can be called synchronously 

    Attributes:
        ID (:obj:`str`): ``ParseTextEntities``

    Args:
        text (:obj:`str`):
            The text to parse 
        parse_mode (:class:`telegram.api.types.TextParseMode`):
            Text parse mode

    Returns:
        FormattedText

    Raises:
        :class:`telegram.Error`
    """
    ID = "parseTextEntities"

    def __init__(self, text, parse_mode, extra=None, **kwargs):
        self.extra = extra
        self.text = text  # str
        self.parse_mode = parse_mode  # TextParseMode

    @staticmethod
    def read(q: dict, *args) -> "ParseTextEntities":
        text = q.get('text')
        parse_mode = Object.read(q.get('parse_mode'))
        return ParseTextEntities(text, parse_mode)
