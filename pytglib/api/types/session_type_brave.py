

from ..utils import Object


class SessionTypeBrave(Object):
    """
    The session is running on the Brave browser

    Attributes:
        ID (:obj:`str`): ``SessionTypeBrave``

    No parameters required.

    Returns:
        SessionType

    Raises:
        :class:`telegram.Error`
    """
    ID = "sessionTypeBrave"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SessionTypeBrave":
        
        return SessionTypeBrave()
