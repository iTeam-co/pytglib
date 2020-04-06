

from ..utils import Object


class GetBankCardInfo(Object):
    """
    Returns information about a bank card 

    Attributes:
        ID (:obj:`str`): ``GetBankCardInfo``

    Args:
        bank_card_number (:obj:`str`):
            The bank card number

    Returns:
        BankCardInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "getBankCardInfo"

    def __init__(self, bank_card_number, extra=None, **kwargs):
        self.extra = extra
        self.bank_card_number = bank_card_number  # str

    @staticmethod
    def read(q: dict, *args) -> "GetBankCardInfo":
        bank_card_number = q.get('bank_card_number')
        return GetBankCardInfo(bank_card_number)
