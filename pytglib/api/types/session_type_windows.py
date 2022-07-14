

from ..utils import Object


class SessionTypeWindows(Object):
    """
    The session is running on a Windows device

    Attributes:
        ID (:obj:`str`): ``SessionTypeWindows``

    No parameters required.

    Returns:
        SessionType

    Raises:
        :class:`telegram.Error`
    """
    ID = "sessionTypeWindows"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SessionTypeWindows":
        
        return SessionTypeWindows()
