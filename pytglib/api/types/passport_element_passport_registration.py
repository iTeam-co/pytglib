

from ..utils import Object


class PassportElementPassportRegistration(Object):
    """
    A Telegram Passport element containing the user's passport registration pages 

    Attributes:
        ID (:obj:`str`): ``PassportElementPassportRegistration``

    Args:
        passport_registration (:class:`telegram.api.types.personalDocument`):
            Passport registration pages

    Returns:
        PassportElement

    Raises:
        :class:`telegram.Error`
    """
    ID = "passportElementPassportRegistration"

    def __init__(self, passport_registration, **kwargs):
        
        self.passport_registration = passport_registration  # PersonalDocument

    @staticmethod
    def read(q: dict, *args) -> "PassportElementPassportRegistration":
        passport_registration = Object.read(q.get('passport_registration'))
        return PassportElementPassportRegistration(passport_registration)
