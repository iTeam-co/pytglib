

from ..utils import Object


class SessionTypeXbox(Object):
    """
    The session is running on an Xbox console

    Attributes:
        ID (:obj:`str`): ``SessionTypeXbox``

    No parameters required.

    Returns:
        SessionType

    Raises:
        :class:`telegram.Error`
    """
    ID = "sessionTypeXbox"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SessionTypeXbox":
        
        return SessionTypeXbox()
