

from ..utils import Object


class PassportElementTypePassport(Object):
    """
    A Telegram Passport element containing the user's passport

    Attributes:
        ID (:obj:`str`): ``PassportElementTypePassport``

    No parameters required.

    Returns:
        PassportElementType

    Raises:
        :class:`telegram.Error`
    """
    ID = "passportElementTypePassport"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PassportElementTypePassport":
        
        return PassportElementTypePassport()
