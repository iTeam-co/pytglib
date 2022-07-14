

from ..utils import Object


class SessionTypeLinux(Object):
    """
    The session is running on a Linux device

    Attributes:
        ID (:obj:`str`): ``SessionTypeLinux``

    No parameters required.

    Returns:
        SessionType

    Raises:
        :class:`telegram.Error`
    """
    ID = "sessionTypeLinux"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SessionTypeLinux":
        
        return SessionTypeLinux()
