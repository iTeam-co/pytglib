

from ..utils import Object


class SessionTypeEdge(Object):
    """
    The session is running on the Edge browser

    Attributes:
        ID (:obj:`str`): ``SessionTypeEdge``

    No parameters required.

    Returns:
        SessionType

    Raises:
        :class:`telegram.Error`
    """
    ID = "sessionTypeEdge"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SessionTypeEdge":
        
        return SessionTypeEdge()
