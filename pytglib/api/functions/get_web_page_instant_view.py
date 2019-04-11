

from ..utils import Object


class GetWebPageInstantView(Object):
    """
    Returns an instant view version of a web page if available. Returns a 404 error if the web page has no instant view page 

    Attributes:
        ID (:obj:`str`): ``GetWebPageInstantView``

    Args:
        url (:obj:`str`):
            The web page URL 
        force_full (:obj:`bool`):
            If true, the full instant view for the web page will be returned

    Returns:
        WebPageInstantView

    Raises:
        :class:`telegram.Error`
    """
    ID = "getWebPageInstantView"

    def __init__(self, url, force_full, extra=None, **kwargs):
        self.extra = extra
        self.url = url  # str
        self.force_full = force_full  # bool

    @staticmethod
    def read(q: dict, *args) -> "GetWebPageInstantView":
        url = q.get('url')
        force_full = q.get('force_full')
        return GetWebPageInstantView(url, force_full)
