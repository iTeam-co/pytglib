

from ..utils import Object


class InputPassportElementError(Object):
    """
    Contains the description of an error in a Telegram Passport element; for bots only 

    Attributes:
        ID (:obj:`str`): ``InputPassportElementError``

    Args:
        type (:class:`telegram.api.types.PassportElementType`):
            Type of Telegram Passport element that has the error 
        message (:obj:`str`):
            Error message 
        source (:class:`telegram.api.types.InputPassportElementErrorSource`):
            Error source

    Returns:
        InputPassportElementError

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputPassportElementError"

    def __init__(self, type, message, source, **kwargs):
        
        self.type = type  # PassportElementType
        self.message = message  # str
        self.source = source  # InputPassportElementErrorSource

    @staticmethod
    def read(q: dict, *args) -> "InputPassportElementError":
        type = Object.read(q.get('type'))
        message = q.get('message')
        source = Object.read(q.get('source'))
        return InputPassportElementError(type, message, source)
