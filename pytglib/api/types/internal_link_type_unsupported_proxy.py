

from ..utils import Object


class InternalLinkTypeUnsupportedProxy(Object):
    """
    The link is a link to an unsupported proxy. An alert can be shown to the user

    Attributes:
        ID (:obj:`str`): ``InternalLinkTypeUnsupportedProxy``

    No parameters required.

    Returns:
        InternalLinkType

    Raises:
        :class:`telegram.Error`
    """
    ID = "internalLinkTypeUnsupportedProxy"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "InternalLinkTypeUnsupportedProxy":
        
        return InternalLinkTypeUnsupportedProxy()
