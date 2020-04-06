

from ..utils import Object


class TextEntityTypeStrikethrough(Object):
    """
    A strikethrough text

    Attributes:
        ID (:obj:`str`): ``TextEntityTypeStrikethrough``

    No parameters required.

    Returns:
        TextEntityType

    Raises:
        :class:`telegram.Error`
    """
    ID = "textEntityTypeStrikethrough"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "TextEntityTypeStrikethrough":
        
        return TextEntityTypeStrikethrough()
