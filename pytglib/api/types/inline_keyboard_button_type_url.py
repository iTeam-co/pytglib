

from ..utils import Object


class InlineKeyboardButtonTypeUrl(Object):
    """
    A button that opens a specified URL 

    Attributes:
        ID (:obj:`str`): ``InlineKeyboardButtonTypeUrl``

    Args:
        url (:obj:`str`):
            HTTP or tg:// URL to open

    Returns:
        InlineKeyboardButtonType

    Raises:
        :class:`telegram.Error`
    """
    ID = "inlineKeyboardButtonTypeUrl"

    def __init__(self, url, **kwargs):
        
        self.url = url  # str

    @staticmethod
    def read(q: dict, *args) -> "InlineKeyboardButtonTypeUrl":
        url = q.get('url')
        return InlineKeyboardButtonTypeUrl(url)
