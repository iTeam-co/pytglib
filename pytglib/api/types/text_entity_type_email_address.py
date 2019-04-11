

from ..utils import Object


class TextEntityTypeEmailAddress(Object):
    """
    An email address

    Attributes:
        ID (:obj:`str`): ``TextEntityTypeEmailAddress``

    No parameters required.

    Returns:
        TextEntityType

    Raises:
        :class:`telegram.Error`
    """
    ID = "textEntityTypeEmailAddress"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "TextEntityTypeEmailAddress":
        
        return TextEntityTypeEmailAddress()
