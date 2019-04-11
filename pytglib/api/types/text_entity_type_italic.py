

from ..utils import Object


class TextEntityTypeItalic(Object):
    """
    An italic text

    Attributes:
        ID (:obj:`str`): ``TextEntityTypeItalic``

    No parameters required.

    Returns:
        TextEntityType

    Raises:
        :class:`telegram.Error`
    """
    ID = "textEntityTypeItalic"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "TextEntityTypeItalic":
        
        return TextEntityTypeItalic()
