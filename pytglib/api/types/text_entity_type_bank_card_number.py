

from ..utils import Object


class TextEntityTypeBankCardNumber(Object):
    """
    A bank card number. The getBankCardInfo method can be used to get information about the bank card

    Attributes:
        ID (:obj:`str`): ``TextEntityTypeBankCardNumber``

    No parameters required.

    Returns:
        TextEntityType

    Raises:
        :class:`telegram.Error`
    """
    ID = "textEntityTypeBankCardNumber"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "TextEntityTypeBankCardNumber":
        
        return TextEntityTypeBankCardNumber()
