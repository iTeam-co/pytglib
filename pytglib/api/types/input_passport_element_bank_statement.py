

from ..utils import Object


class InputPassportElementBankStatement(Object):
    """
    A Telegram Passport element to be saved containing the user's bank statement 

    Attributes:
        ID (:obj:`str`): ``InputPassportElementBankStatement``

    Args:
        bank_statement (:class:`telegram.api.types.inputPersonalDocument`):
            The bank statement to be saved

    Returns:
        InputPassportElement

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputPassportElementBankStatement"

    def __init__(self, bank_statement, **kwargs):
        
        self.bank_statement = bank_statement  # InputPersonalDocument

    @staticmethod
    def read(q: dict, *args) -> "InputPassportElementBankStatement":
        bank_statement = Object.read(q.get('bank_statement'))
        return InputPassportElementBankStatement(bank_statement)
