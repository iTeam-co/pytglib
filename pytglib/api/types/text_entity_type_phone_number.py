

from ..utils import Object


class TextEntityTypePhoneNumber(Object):
    """
    A phone number

    Attributes:
        ID (:obj:`str`): ``TextEntityTypePhoneNumber``

    No parameters required.

    Returns:
        TextEntityType

    Raises:
        :class:`telegram.Error`
    """
    ID = "textEntityTypePhoneNumber"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "TextEntityTypePhoneNumber":
        
        return TextEntityTypePhoneNumber()
