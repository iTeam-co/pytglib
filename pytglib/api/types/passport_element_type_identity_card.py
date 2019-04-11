

from ..utils import Object


class PassportElementTypeIdentityCard(Object):
    """
    A Telegram Passport element containing the user's identity card

    Attributes:
        ID (:obj:`str`): ``PassportElementTypeIdentityCard``

    No parameters required.

    Returns:
        PassportElementType

    Raises:
        :class:`telegram.Error`
    """
    ID = "passportElementTypeIdentityCard"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PassportElementTypeIdentityCard":
        
        return PassportElementTypeIdentityCard()
