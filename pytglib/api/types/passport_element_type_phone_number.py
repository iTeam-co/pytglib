

from ..utils import Object


class PassportElementTypePhoneNumber(Object):
    """
    A Telegram Passport element containing the user's phone number

    Attributes:
        ID (:obj:`str`): ``PassportElementTypePhoneNumber``

    No parameters required.

    Returns:
        PassportElementType

    Raises:
        :class:`telegram.Error`
    """
    ID = "passportElementTypePhoneNumber"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PassportElementTypePhoneNumber":
        
        return PassportElementTypePhoneNumber()
