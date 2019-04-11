

from ..utils import Object


class PassportElementPhoneNumber(Object):
    """
    A Telegram Passport element containing the user's phone number 

    Attributes:
        ID (:obj:`str`): ``PassportElementPhoneNumber``

    Args:
        phone_number (:obj:`str`):
            Phone number

    Returns:
        PassportElement

    Raises:
        :class:`telegram.Error`
    """
    ID = "passportElementPhoneNumber"

    def __init__(self, phone_number, **kwargs):
        
        self.phone_number = phone_number  # str

    @staticmethod
    def read(q: dict, *args) -> "PassportElementPhoneNumber":
        phone_number = q.get('phone_number')
        return PassportElementPhoneNumber(phone_number)
