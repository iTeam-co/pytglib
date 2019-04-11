

from ..utils import Object


class TextEntityTypePreCode(Object):
    """
    Text that must be formatted as if inside pre, and code HTML tags 

    Attributes:
        ID (:obj:`str`): ``TextEntityTypePreCode``

    Args:
        language (:obj:`str`):
            Programming language of the code; as defined by the sender

    Returns:
        TextEntityType

    Raises:
        :class:`telegram.Error`
    """
    ID = "textEntityTypePreCode"

    def __init__(self, language, **kwargs):
        
        self.language = language  # str

    @staticmethod
    def read(q: dict, *args) -> "TextEntityTypePreCode":
        language = q.get('language')
        return TextEntityTypePreCode(language)
