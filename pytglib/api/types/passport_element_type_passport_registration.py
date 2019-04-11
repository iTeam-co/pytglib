

from ..utils import Object


class PassportElementTypePassportRegistration(Object):
    """
    A Telegram Passport element containing the registration page of the user's passport

    Attributes:
        ID (:obj:`str`): ``PassportElementTypePassportRegistration``

    No parameters required.

    Returns:
        PassportElementType

    Raises:
        :class:`telegram.Error`
    """
    ID = "passportElementTypePassportRegistration"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PassportElementTypePassportRegistration":
        
        return PassportElementTypePassportRegistration()
