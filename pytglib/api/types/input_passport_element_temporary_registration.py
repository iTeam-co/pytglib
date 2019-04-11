

from ..utils import Object


class InputPassportElementTemporaryRegistration(Object):
    """
    A Telegram Passport element to be saved containing the user's temporary registration 

    Attributes:
        ID (:obj:`str`): ``InputPassportElementTemporaryRegistration``

    Args:
        temporary_registration (:class:`telegram.api.types.inputPersonalDocument`):
            The temporary registration document to be saved

    Returns:
        InputPassportElement

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputPassportElementTemporaryRegistration"

    def __init__(self, temporary_registration, **kwargs):
        
        self.temporary_registration = temporary_registration  # InputPersonalDocument

    @staticmethod
    def read(q: dict, *args) -> "InputPassportElementTemporaryRegistration":
        temporary_registration = Object.read(q.get('temporary_registration'))
        return InputPassportElementTemporaryRegistration(temporary_registration)
