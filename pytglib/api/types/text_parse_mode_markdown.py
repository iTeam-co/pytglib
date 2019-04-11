

from ..utils import Object


class TextParseModeMarkdown(Object):
    """
    The text should be parsed in markdown-style

    Attributes:
        ID (:obj:`str`): ``TextParseModeMarkdown``

    No parameters required.

    Returns:
        TextParseMode

    Raises:
        :class:`telegram.Error`
    """
    ID = "textParseModeMarkdown"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "TextParseModeMarkdown":
        
        return TextParseModeMarkdown()
