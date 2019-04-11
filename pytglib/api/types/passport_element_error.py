

from ..utils import Object


class PassportElementError(Object):
    """
    Contains the description of an error in a Telegram Passport element 

    Attributes:
        ID (:obj:`str`): ``PassportElementError``

    Args:
        type (:class:`telegram.api.types.PassportElementType`):
            Type of the Telegram Passport element which has the error 
        message (:obj:`str`):
            Error message 
        source (:class:`telegram.api.types.PassportElementErrorSource`):
            Error source

    Returns:
        PassportElementError

    Raises:
        :class:`telegram.Error`
    """
    ID = "passportElementError"

    def __init__(self, type, message, source, **kwargs):
        
        self.type = type  # PassportElementType
        self.message = message  # str
        self.source = source  # PassportElementErrorSource

    @staticmethod
    def read(q: dict, *args) -> "PassportElementError":
        type = Object.read(q.get('type'))
        message = q.get('message')
        source = Object.read(q.get('source'))
        return PassportElementError(type, message, source)
