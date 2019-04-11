

from ..utils import Object


class PassportElementTypeDriverLicense(Object):
    """
    A Telegram Passport element containing the user's driver license

    Attributes:
        ID (:obj:`str`): ``PassportElementTypeDriverLicense``

    No parameters required.

    Returns:
        PassportElementType

    Raises:
        :class:`telegram.Error`
    """
    ID = "passportElementTypeDriverLicense"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PassportElementTypeDriverLicense":
        
        return PassportElementTypeDriverLicense()
