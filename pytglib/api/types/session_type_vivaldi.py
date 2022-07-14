

from ..utils import Object


class SessionTypeVivaldi(Object):
    """
    The session is running on the Vivaldi browser

    Attributes:
        ID (:obj:`str`): ``SessionTypeVivaldi``

    No parameters required.

    Returns:
        SessionType

    Raises:
        :class:`telegram.Error`
    """
    ID = "sessionTypeVivaldi"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SessionTypeVivaldi":
        
        return SessionTypeVivaldi()
