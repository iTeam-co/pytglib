

from ..utils import Object


class SessionTypeUnknown(Object):
    """
    The session is running on an unknown type of device

    Attributes:
        ID (:obj:`str`): ``SessionTypeUnknown``

    No parameters required.

    Returns:
        SessionType

    Raises:
        :class:`telegram.Error`
    """
    ID = "sessionTypeUnknown"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SessionTypeUnknown":
        
        return SessionTypeUnknown()
