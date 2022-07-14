

from ..utils import Object


class SessionTypeFirefox(Object):
    """
    The session is running on the Firefox browser

    Attributes:
        ID (:obj:`str`): ``SessionTypeFirefox``

    No parameters required.

    Returns:
        SessionType

    Raises:
        :class:`telegram.Error`
    """
    ID = "sessionTypeFirefox"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SessionTypeFirefox":
        
        return SessionTypeFirefox()
