

from ..utils import Object


class PassportElementTypeEmailAddress(Object):
    """
    A Telegram Passport element containing the user's email address

    Attributes:
        ID (:obj:`str`): ``PassportElementTypeEmailAddress``

    No parameters required.

    Returns:
        PassportElementType

    Raises:
        :class:`telegram.Error`
    """
    ID = "passportElementTypeEmailAddress"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PassportElementTypeEmailAddress":
        
        return PassportElementTypeEmailAddress()
