

from ..utils import Object


class SessionTypeUbuntu(Object):
    """
    The session is running on an Ubuntu device

    Attributes:
        ID (:obj:`str`): ``SessionTypeUbuntu``

    No parameters required.

    Returns:
        SessionType

    Raises:
        :class:`telegram.Error`
    """
    ID = "sessionTypeUbuntu"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SessionTypeUbuntu":
        
        return SessionTypeUbuntu()
