

from ..utils import Object


class PassportElementBankStatement(Object):
    """
    A Telegram Passport element containing the user's bank statement 

    Attributes:
        ID (:obj:`str`): ``PassportElementBankStatement``

    Args:
        bank_statement (:class:`telegram.api.types.personalDocument`):
            Bank statement

    Returns:
        PassportElement

    Raises:
        :class:`telegram.Error`
    """
    ID = "passportElementBankStatement"

    def __init__(self, bank_statement, **kwargs):
        
        self.bank_statement = bank_statement  # PersonalDocument

    @staticmethod
    def read(q: dict, *args) -> "PassportElementBankStatement":
        bank_statement = Object.read(q.get('bank_statement'))
        return PassportElementBankStatement(bank_statement)
