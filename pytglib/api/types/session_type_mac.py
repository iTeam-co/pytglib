

from ..utils import Object


class SessionTypeMac(Object):
    """
    The session is running on a Mac device

    Attributes:
        ID (:obj:`str`): ``SessionTypeMac``

    No parameters required.

    Returns:
        SessionType

    Raises:
        :class:`telegram.Error`
    """
    ID = "sessionTypeMac"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SessionTypeMac":
        
        return SessionTypeMac()
