

from ..utils import Object


class InputPassportElementInternalPassport(Object):
    """
    A Telegram Passport element to be saved containing the user's internal passport 

    Attributes:
        ID (:obj:`str`): ``InputPassportElementInternalPassport``

    Args:
        internal_passport (:class:`telegram.api.types.inputIdentityDocument`):
            The internal passport to be saved

    Returns:
        InputPassportElement

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputPassportElementInternalPassport"

    def __init__(self, internal_passport, **kwargs):
        
        self.internal_passport = internal_passport  # InputIdentityDocument

    @staticmethod
    def read(q: dict, *args) -> "InputPassportElementInternalPassport":
        internal_passport = Object.read(q.get('internal_passport'))
        return InputPassportElementInternalPassport(internal_passport)
