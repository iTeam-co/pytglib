

from ..utils import Object


class PassportElementTypeBankStatement(Object):
    """
    A Telegram Passport element containing the user's bank statement

    Attributes:
        ID (:obj:`str`): ``PassportElementTypeBankStatement``

    No parameters required.

    Returns:
        PassportElementType

    Raises:
        :class:`telegram.Error`
    """
    ID = "passportElementTypeBankStatement"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PassportElementTypeBankStatement":
        
        return PassportElementTypeBankStatement()
