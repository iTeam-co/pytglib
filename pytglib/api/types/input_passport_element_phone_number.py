

from ..utils import Object


class InputPassportElementPhoneNumber(Object):
    """
    A Telegram Passport element to be saved containing the user's phone number 

    Attributes:
        ID (:obj:`str`): ``InputPassportElementPhoneNumber``

    Args:
        phone_number (:obj:`str`):
            The phone number to be saved

    Returns:
        InputPassportElement

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputPassportElementPhoneNumber"

    def __init__(self, phone_number, **kwargs):
        
        self.phone_number = phone_number  # str

    @staticmethod
    def read(q: dict, *args) -> "InputPassportElementPhoneNumber":
        phone_number = q.get('phone_number')
        return InputPassportElementPhoneNumber(phone_number)
