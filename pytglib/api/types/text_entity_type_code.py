

from ..utils import Object


class TextEntityTypeCode(Object):
    """
    Text that must be formatted as if inside a code HTML tag

    Attributes:
        ID (:obj:`str`): ``TextEntityTypeCode``

    No parameters required.

    Returns:
        TextEntityType

    Raises:
        :class:`telegram.Error`
    """
    ID = "textEntityTypeCode"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "TextEntityTypeCode":
        
        return TextEntityTypeCode()
