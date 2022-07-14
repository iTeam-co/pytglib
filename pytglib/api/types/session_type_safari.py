

from ..utils import Object


class SessionTypeSafari(Object):
    """
    The session is running on the Safari browser

    Attributes:
        ID (:obj:`str`): ``SessionTypeSafari``

    No parameters required.

    Returns:
        SessionType

    Raises:
        :class:`telegram.Error`
    """
    ID = "sessionTypeSafari"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SessionTypeSafari":
        
        return SessionTypeSafari()
