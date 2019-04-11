

from ..utils import Object


class PassportElementTypeInternalPassport(Object):
    """
    A Telegram Passport element containing the user's internal passport

    Attributes:
        ID (:obj:`str`): ``PassportElementTypeInternalPassport``

    No parameters required.

    Returns:
        PassportElementType

    Raises:
        :class:`telegram.Error`
    """
    ID = "passportElementTypeInternalPassport"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PassportElementTypeInternalPassport":
        
        return PassportElementTypeInternalPassport()
