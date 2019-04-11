

from ..utils import Object


class PassportElementTypeUtilityBill(Object):
    """
    A Telegram Passport element containing the user's utility bill

    Attributes:
        ID (:obj:`str`): ``PassportElementTypeUtilityBill``

    No parameters required.

    Returns:
        PassportElementType

    Raises:
        :class:`telegram.Error`
    """
    ID = "passportElementTypeUtilityBill"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PassportElementTypeUtilityBill":
        
        return PassportElementTypeUtilityBill()
