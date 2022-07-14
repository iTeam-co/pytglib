

from ..utils import Object


class GetExternalLinkInfo(Object):
    """
    Returns information about an action to be done when the current user clicks an external link. Don't use this method for links from secret chats if web page preview is disabled in secret chats 

    Attributes:
        ID (:obj:`str`): ``GetExternalLinkInfo``

    Args:
        link (:obj:`str`):
            The link

    Returns:
        LoginUrlInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "getExternalLinkInfo"

    def __init__(self, link, extra=None, **kwargs):
        self.extra = extra
        self.link = link  # str

    @staticmethod
    def read(q: dict, *args) -> "GetExternalLinkInfo":
        link = q.get('link')
        return GetExternalLinkInfo(link)
