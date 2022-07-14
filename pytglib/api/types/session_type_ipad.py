

from ..utils import Object


class SessionTypeIpad(Object):
    """
    The session is running on an iPad device

    Attributes:
        ID (:obj:`str`): ``SessionTypeIpad``

    No parameters required.

    Returns:
        SessionType

    Raises:
        :class:`telegram.Error`
    """
    ID = "sessionTypeIpad"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SessionTypeIpad":
        
        return SessionTypeIpad()
