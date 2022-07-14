

from ..utils import Object


class TextEntityTypeSpoiler(Object):
    """
    A spoiler text. Not supported in secret chats

    Attributes:
        ID (:obj:`str`): ``TextEntityTypeSpoiler``

    No parameters required.

    Returns:
        TextEntityType

    Raises:
        :class:`telegram.Error`
    """
    ID = "textEntityTypeSpoiler"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "TextEntityTypeSpoiler":
        
        return TextEntityTypeSpoiler()
