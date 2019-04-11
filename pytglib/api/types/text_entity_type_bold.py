

from ..utils import Object


class TextEntityTypeBold(Object):
    """
    A bold text

    Attributes:
        ID (:obj:`str`): ``TextEntityTypeBold``

    No parameters required.

    Returns:
        TextEntityType

    Raises:
        :class:`telegram.Error`
    """
    ID = "textEntityTypeBold"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "TextEntityTypeBold":
        
        return TextEntityTypeBold()
