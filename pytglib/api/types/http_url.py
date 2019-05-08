

from ..utils import Object


class HttpUrl(Object):
    """
    Contains an HTTP URL 

    Attributes:
        ID (:obj:`str`): ``HttpUrl``

    Args:
        url (:obj:`str`):
            The URL

    Returns:
        HttpUrl

    Raises:
        :class:`telegram.Error`
    """
    ID = "httpUrl"

    def __init__(self, url, **kwargs):
        
        self.url = url  # str

    @staticmethod
    def read(q: dict, *args) -> "HttpUrl":
        url = q.get('url')
        return HttpUrl(url)
