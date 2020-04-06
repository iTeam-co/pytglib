

from ..utils import Object


class TextParseModeHTML(Object):
    """
    The text uses HTML-style formatting. The same as Telegram Bot API "HTML" parse mode

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
