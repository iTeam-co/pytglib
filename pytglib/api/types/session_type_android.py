

from ..utils import Object


class SessionTypeAndroid(Object):
    """
    The session is running on an Android device

    Attributes:
        ID (:obj:`str`): ``SessionTypeAndroid``

    No parameters required.

    Returns:
        SessionType

    Raises:
        :class:`telegram.Error`
    """
    ID = "sessionTypeAndroid"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SessionTypeAndroid":
        
        return SessionTypeAndroid()
