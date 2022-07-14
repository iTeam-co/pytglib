

from ..utils import Object


class InlineKeyboardButtonTypeWebApp(Object):
    """
    A button that opens a Web App by calling openWebApp 

    Attributes:
        ID (:obj:`str`): ``InlineKeyboardButtonTypeWebApp``

    Args:
        url (:obj:`str`):
            An HTTP URL to pass to openWebApp

    Returns:
        InlineKeyboardButtonType

    Raises:
        :class:`telegram.Error`
    """
    ID = "inlineKeyboardButtonTypeWebApp"

    def __init__(self, url, **kwargs):
        
        self.url = url  # str

    @staticmethod
    def read(q: dict, *args) -> "InlineKeyboardButtonTypeWebApp":
        url = q.get('url')
        return InlineKeyboardButtonTypeWebApp(url)
