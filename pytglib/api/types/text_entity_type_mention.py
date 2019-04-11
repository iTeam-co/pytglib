

from ..utils import Object


class TextEntityTypeMention(Object):
    """
    A mention of a user by their username

    Attributes:
        ID (:obj:`str`): ``TextEntityTypeMention``

    No parameters required.

    Returns:
        TextEntityType

    Raises:
        :class:`telegram.Error`
    """
    ID = "textEntityTypeMention"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "TextEntityTypeMention":
        
        return TextEntityTypeMention()
