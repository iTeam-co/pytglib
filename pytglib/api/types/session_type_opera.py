

from ..utils import Object


class SessionTypeOpera(Object):
    """
    The session is running on the Opera browser

    Attributes:
        ID (:obj:`str`): ``SessionTypeOpera``

    No parameters required.

    Returns:
        SessionType

    Raises:
        :class:`telegram.Error`
    """
    ID = "sessionTypeOpera"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SessionTypeOpera":
        
        return SessionTypeOpera()
