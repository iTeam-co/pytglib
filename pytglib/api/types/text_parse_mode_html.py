

from ..utils import Object


class TextParseModeHTML(Object):
    """
    The text should be parsed in HTML-style

    Attributes:
        ID (:obj:`str`): ``TextParseModeHTML``

    No parameters required.

    Returns:
        TextParseMode

    Raises:
        :class:`telegram.Error`
    """
    ID = "textParseModeHTML"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "TextParseModeHTML":
        
        return TextParseModeHTML()
