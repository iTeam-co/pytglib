

from ..utils import Object


class GetInternalLinkType(Object):
    """
    Returns information about the type of an internal link. Returns a 404 error if the link is not internal. Can be called before authorization 

    Attributes:
        ID (:obj:`str`): ``GetInternalLinkType``

    Args:
        link (:obj:`str`):
            The link

    Returns:
        InternalLinkType

    Raises:
        :class:`telegram.Error`
    """
    ID = "getInternalLinkType"

    def __init__(self, link, extra=None, **kwargs):
        self.extra = extra
        self.link = link  # str

    @staticmethod
    def read(q: dict, *args) -> "GetInternalLinkType":
        link = q.get('link')
        return GetInternalLinkType(link)
