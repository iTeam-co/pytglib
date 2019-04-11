

from ..utils import Object


class GetActiveSessions(Object):
    """
    Returns all active sessions of the current user

    Attributes:
        ID (:obj:`str`): ``GetActiveSessions``

    No parameters required.

    Returns:
        Sessions

    Raises:
        :class:`telegram.Error`
    """
    ID = "getActiveSessions"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "GetActiveSessions":
        
        return GetActiveSessions()
