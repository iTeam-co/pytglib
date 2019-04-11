

from ..utils import Object


class PassportElementTypePersonalDetails(Object):
    """
    A Telegram Passport element containing the user's personal details

    Attributes:
        ID (:obj:`str`): ``PassportElementTypePersonalDetails``

    No parameters required.

    Returns:
        PassportElementType

    Raises:
        :class:`telegram.Error`
    """
    ID = "passportElementTypePersonalDetails"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PassportElementTypePersonalDetails":
        
        return PassportElementTypePersonalDetails()
