

from ..utils import Object


class PassportElementTypeAddress(Object):
    """
    A Telegram Passport element containing the user's address

    Attributes:
        ID (:obj:`str`): ``PassportElementTypeAddress``

    No parameters required.

    Returns:
        PassportElementType

    Raises:
        :class:`telegram.Error`
    """
    ID = "passportElementTypeAddress"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PassportElementTypeAddress":
        
        return PassportElementTypeAddress()
