

from ..utils import Object


class InputPassportElementUtilityBill(Object):
    """
    A Telegram Passport element to be saved containing the user's utility bill 

    Attributes:
        ID (:obj:`str`): ``InputPassportElementUtilityBill``

    Args:
        utility_bill (:class:`telegram.api.types.inputPersonalDocument`):
            The utility bill to be saved

    Returns:
        InputPassportElement

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputPassportElementUtilityBill"

    def __init__(self, utility_bill, **kwargs):
        
        self.utility_bill = utility_bill  # InputPersonalDocument

    @staticmethod
    def read(q: dict, *args) -> "InputPassportElementUtilityBill":
        utility_bill = Object.read(q.get('utility_bill'))
        return InputPassportElementUtilityBill(utility_bill)
