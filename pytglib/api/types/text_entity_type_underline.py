

from ..utils import Object


class TextEntityTypeUnderline(Object):
    """
    An underlined text

    Attributes:
        ID (:obj:`str`): ``TextEntityTypeUnderline``

    No parameters required.

    Returns:
        TextEntityType

    Raises:
        :class:`telegram.Error`
    """
    ID = "textEntityTypeUnderline"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "TextEntityTypeUnderline":
        
        return TextEntityTypeUnderline()
