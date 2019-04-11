

from ..utils import Object


class GetPassportElement(Object):
    """
    Returns one of the available Telegram Passport elements 

    Attributes:
        ID (:obj:`str`): ``GetPassportElement``

    Args:
        type (:class:`telegram.api.types.PassportElementType`):
            Telegram Passport element type 
        password (:obj:`str`):
            Password of the current user

    Returns:
        PassportElement

    Raises:
        :class:`telegram.Error`
    """
    ID = "getPassportElement"

    def __init__(self, type, password, extra=None, **kwargs):
        self.extra = extra
        self.type = type  # PassportElementType
        self.password = password  # str

    @staticmethod
    def read(q: dict, *args) -> "GetPassportElement":
        type = Object.read(q.get('type'))
        password = q.get('password')
        return GetPassportElement(type, password)
