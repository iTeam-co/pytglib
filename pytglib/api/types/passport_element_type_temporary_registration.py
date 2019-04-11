

from ..utils import Object


class PassportElementTypeTemporaryRegistration(Object):
    """
    A Telegram Passport element containing the user's temporary registration

    Attributes:
        ID (:obj:`str`): ``PassportElementTypeTemporaryRegistration``

    No parameters required.

    Returns:
        PassportElementType

    Raises:
        :class:`telegram.Error`
    """
    ID = "passportElementTypeTemporaryRegistration"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PassportElementTypeTemporaryRegistration":
        
        return PassportElementTypeTemporaryRegistration()
