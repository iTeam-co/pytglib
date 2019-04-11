

from ..utils import Object


class InputPassportElementPassportRegistration(Object):
    """
    A Telegram Passport element to be saved containing the user's passport registration 

    Attributes:
        ID (:obj:`str`): ``InputPassportElementPassportRegistration``

    Args:
        passport_registration (:class:`telegram.api.types.inputPersonalDocument`):
            The passport registration page to be saved

    Returns:
        InputPassportElement

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputPassportElementPassportRegistration"

    def __init__(self, passport_registration, **kwargs):
        
        self.passport_registration = passport_registration  # InputPersonalDocument

    @staticmethod
    def read(q: dict, *args) -> "InputPassportElementPassportRegistration":
        passport_registration = Object.read(q.get('passport_registration'))
        return InputPassportElementPassportRegistration(passport_registration)
