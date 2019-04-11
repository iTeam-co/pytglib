

from ..utils import Object


class PassportElementEmailAddress(Object):
    """
    A Telegram Passport element containing the user's email address 

    Attributes:
        ID (:obj:`str`): ``PassportElementEmailAddress``

    Args:
        email_address (:obj:`str`):
            Email address

    Returns:
        PassportElement

    Raises:
        :class:`telegram.Error`
    """
    ID = "passportElementEmailAddress"

    def __init__(self, email_address, **kwargs):
        
        self.email_address = email_address  # str

    @staticmethod
    def read(q: dict, *args) -> "PassportElementEmailAddress":
        email_address = q.get('email_address')
        return PassportElementEmailAddress(email_address)
