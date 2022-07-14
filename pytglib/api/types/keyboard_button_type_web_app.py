

from ..utils import Object


class KeyboardButtonTypeWebApp(Object):
    """
    A button that opens a Web App by calling getWebAppUrl 

    Attributes:
        ID (:obj:`str`): ``KeyboardButtonTypeWebApp``

    Args:
        url (:obj:`str`):
            An HTTP URL to pass to getWebAppUrl

    Returns:
        KeyboardButtonType

    Raises:
        :class:`telegram.Error`
    """
    ID = "keyboardButtonTypeWebApp"

    def __init__(self, url, **kwargs):
        
        self.url = url  # str

    @staticmethod
    def read(q: dict, *args) -> "KeyboardButtonTypeWebApp":
        url = q.get('url')
        return KeyboardButtonTypeWebApp(url)
