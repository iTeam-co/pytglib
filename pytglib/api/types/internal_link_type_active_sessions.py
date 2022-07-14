

from ..utils import Object


class InternalLinkTypeActiveSessions(Object):
    """
    The link is a link to the active sessions section of the application. Use getActiveSessions to handle the link

    Attributes:
        ID (:obj:`str`): ``InternalLinkTypeActiveSessions``

    No parameters required.

    Returns:
        InternalLinkType

    Raises:
        :class:`telegram.Error`
    """
    ID = "internalLinkTypeActiveSessions"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "InternalLinkTypeActiveSessions":
        
        return InternalLinkTypeActiveSessions()
