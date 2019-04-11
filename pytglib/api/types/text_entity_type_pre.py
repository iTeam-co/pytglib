

from ..utils import Object


class TextEntityTypePre(Object):
    """
    Text that must be formatted as if inside a pre HTML tag

    Attributes:
        ID (:obj:`str`): ``TextEntityTypePre``

    No parameters required.

    Returns:
        TextEntityType

    Raises:
        :class:`telegram.Error`
    """
    ID = "textEntityTypePre"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "TextEntityTypePre":
        
        return TextEntityTypePre()
