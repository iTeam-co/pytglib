

from ..utils import Object


class SessionTypeIphone(Object):
    """
    The session is running on an iPhone device

    Attributes:
        ID (:obj:`str`): ``SessionTypeIphone``

    No parameters required.

    Returns:
        SessionType

    Raises:
        :class:`telegram.Error`
    """
    ID = "sessionTypeIphone"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SessionTypeIphone":
        
        return SessionTypeIphone()
