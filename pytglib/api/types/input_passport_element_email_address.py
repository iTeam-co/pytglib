

from ..utils import Object


class InputPassportElementEmailAddress(Object):
    """
    A Telegram Passport element to be saved containing the user's email address 

    Attributes:
        ID (:obj:`str`): ``InputPassportElementEmailAddress``

    Args:
        email_address (:obj:`str`):
            The email address to be saved

    Returns:
        InputPassportElement

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputPassportElementEmailAddress"

    def __init__(self, email_address, **kwargs):
        
        self.email_address = email_address  # str

    @staticmethod
    def read(q: dict, *args) -> "InputPassportElementEmailAddress":
        email_address = q.get('email_address')
        return InputPassportElementEmailAddress(email_address)
