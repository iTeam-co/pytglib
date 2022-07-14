

from ..utils import Object


class InternalLinkTypeUnknownDeepLink(Object):
    """
    The link is an unknown tg: link. Call getDeepLinkInfo to process the link 

    Attributes:
        ID (:obj:`str`): ``InternalLinkTypeUnknownDeepLink``

    Args:
        link (:obj:`str`):
            Link to be passed to getDeepLinkInfo

    Returns:
        InternalLinkType

    Raises:
        :class:`telegram.Error`
    """
    ID = "internalLinkTypeUnknownDeepLink"

    def __init__(self, link, **kwargs):
        
        self.link = link  # str

    @staticmethod
    def read(q: dict, *args) -> "InternalLinkTypeUnknownDeepLink":
        link = q.get('link')
        return InternalLinkTypeUnknownDeepLink(link)
