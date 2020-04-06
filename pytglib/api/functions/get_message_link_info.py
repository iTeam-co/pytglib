

from ..utils import Object


class GetMessageLinkInfo(Object):
    """
    Returns information about a public or private message link 

    Attributes:
        ID (:obj:`str`): ``GetMessageLinkInfo``

    Args:
        url (:obj:`str`):
            The message link in the format "https://tme/c/", or "tg://privatepost?", or "https://tme/username/", or "tg://resolve?"

    Returns:
        MessageLinkInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "getMessageLinkInfo"

    def __init__(self, url, extra=None, **kwargs):
        self.extra = extra
        self.url = url  # str

    @staticmethod
    def read(q: dict, *args) -> "GetMessageLinkInfo":
        url = q.get('url')
        return GetMessageLinkInfo(url)
