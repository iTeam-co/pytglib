

from ..utils import Object


class SessionTypeApple(Object):
    """
    The session is running on a generic Apple device

    Attributes:
        ID (:obj:`str`): ``SessionTypeApple``

    No parameters required.

    Returns:
        SessionType

    Raises:
        :class:`telegram.Error`
    """
    ID = "sessionTypeApple"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SessionTypeApple":
        
        return SessionTypeApple()
