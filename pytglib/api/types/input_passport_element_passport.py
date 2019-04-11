

from ..utils import Object


class InputPassportElementPassport(Object):
    """
    A Telegram Passport element to be saved containing the user's passport 

    Attributes:
        ID (:obj:`str`): ``InputPassportElementPassport``

    Args:
        passport (:class:`telegram.api.types.inputIdentityDocument`):
            The passport to be saved

    Returns:
        InputPassportElement

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputPassportElementPassport"

    def __init__(self, passport, **kwargs):
        
        self.passport = passport  # InputIdentityDocument

    @staticmethod
    def read(q: dict, *args) -> "InputPassportElementPassport":
        passport = Object.read(q.get('passport'))
        return InputPassportElementPassport(passport)
