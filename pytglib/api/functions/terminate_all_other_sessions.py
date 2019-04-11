

from ..utils import Object


class TerminateAllOtherSessions(Object):
    """
    Terminates all other sessions of the current user

    Attributes:
        ID (:obj:`str`): ``TerminateAllOtherSessions``

    No parameters required.

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "terminateAllOtherSessions"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "TerminateAllOtherSessions":
        
        return TerminateAllOtherSessions()
