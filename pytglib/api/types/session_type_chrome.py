

from ..utils import Object


class SessionTypeChrome(Object):
    """
    The session is running on the Chrome browser

    Attributes:
        ID (:obj:`str`): ``SessionTypeChrome``

    No parameters required.

    Returns:
        SessionType

    Raises:
        :class:`telegram.Error`
    """
    ID = "sessionTypeChrome"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SessionTypeChrome":
        
        return SessionTypeChrome()
