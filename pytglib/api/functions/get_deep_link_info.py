

from ..utils import Object


class GetDeepLinkInfo(Object):
    """
    Returns information about a tg:// deep link. Use "tg://need_update_for_some_feature" or "tg:some_unsupported_feature" for testing. Returns a 404 error for unknown links. Can be called before authorization 

    Attributes:
        ID (:obj:`str`): ``GetDeepLinkInfo``

    Args:
        link (:obj:`str`):
            The link

    Returns:
        DeepLinkInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "getDeepLinkInfo"

    def __init__(self, link, extra=None, **kwargs):
        self.extra = extra
        self.link = link  # str

    @staticmethod
    def read(q: dict, *args) -> "GetDeepLinkInfo":
        link = q.get('link')
        return GetDeepLinkInfo(link)
