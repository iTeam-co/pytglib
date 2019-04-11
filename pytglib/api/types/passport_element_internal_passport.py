

from ..utils import Object


class PassportElementInternalPassport(Object):
    """
    A Telegram Passport element containing the user's internal passport 

    Attributes:
        ID (:obj:`str`): ``PassportElementInternalPassport``

    Args:
        internal_passport (:class:`telegram.api.types.identityDocument`):
            Internal passport

    Returns:
        PassportElement

    Raises:
        :class:`telegram.Error`
    """
    ID = "passportElementInternalPassport"

    def __init__(self, internal_passport, **kwargs):
        
        self.internal_passport = internal_passport  # IdentityDocument

    @staticmethod
    def read(q: dict, *args) -> "PassportElementInternalPassport":
        internal_passport = Object.read(q.get('internal_passport'))
        return PassportElementInternalPassport(internal_passport)
