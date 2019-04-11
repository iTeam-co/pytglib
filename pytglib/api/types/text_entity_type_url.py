

from ..utils import Object


class TextEntityTypeUrl(Object):
    """
    An HTTP URL

    Attributes:
        ID (:obj:`str`): ``TextEntityTypeUrl``

    No parameters required.

    Returns:
        TextEntityType

    Raises:
        :class:`telegram.Error`
    """
    ID = "textEntityTypeUrl"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "TextEntityTypeUrl":
        
        return TextEntityTypeUrl()
