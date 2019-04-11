

from ..utils import Object


class PassportElementPassport(Object):
    """
    A Telegram Passport element containing the user's passport 

    Attributes:
        ID (:obj:`str`): ``PassportElementPassport``

    Args:
        passport (:class:`telegram.api.types.identityDocument`):
            Passport

    Returns:
        PassportElement

    Raises:
        :class:`telegram.Error`
    """
    ID = "passportElementPassport"

    def __init__(self, passport, **kwargs):
        
        self.passport = passport  # IdentityDocument

    @staticmethod
    def read(q: dict, *args) -> "PassportElementPassport":
        passport = Object.read(q.get('passport'))
        return PassportElementPassport(passport)
