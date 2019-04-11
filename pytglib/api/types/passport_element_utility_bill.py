

from ..utils import Object


class PassportElementUtilityBill(Object):
    """
    A Telegram Passport element containing the user's utility bill 

    Attributes:
        ID (:obj:`str`): ``PassportElementUtilityBill``

    Args:
        utility_bill (:class:`telegram.api.types.personalDocument`):
            Utility bill

    Returns:
        PassportElement

    Raises:
        :class:`telegram.Error`
    """
    ID = "passportElementUtilityBill"

    def __init__(self, utility_bill, **kwargs):
        
        self.utility_bill = utility_bill  # PersonalDocument

    @staticmethod
    def read(q: dict, *args) -> "PassportElementUtilityBill":
        utility_bill = Object.read(q.get('utility_bill'))
        return PassportElementUtilityBill(utility_bill)
