

from ..utils import Object


class TMeUrls(Object):
    """
    Contains a list of t.me URLs 

    Attributes:
        ID (:obj:`str`): ``TMeUrls``

    Args:
        urls (List of :class:`telegram.api.types.tMeUrl`):
            List of URLs

    Returns:
        TMeUrls

    Raises:
        :class:`telegram.Error`
    """
    ID = "tMeUrls"

    def __init__(self, urls, **kwargs):
        
        self.urls = urls  # list of tMeUrl

    @staticmethod
    def read(q: dict, *args) -> "TMeUrls":
        urls = [Object.read(i) for i in q.get('urls', [])]
        return TMeUrls(urls)
