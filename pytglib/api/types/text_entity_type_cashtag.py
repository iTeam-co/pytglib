

from ..utils import Object


class TextEntityTypeCashtag(Object):
    """
    A cashtag text, beginning with "$" and consisting of capital English letters (e.g., "$USD")

    Attributes:
        ID (:obj:`str`): ``TextEntityTypeCashtag``

    No parameters required.

    Returns:
        TextEntityType

    Raises:
        :class:`telegram.Error`
    """
    ID = "textEntityTypeCashtag"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "TextEntityTypeCashtag":
        
        return TextEntityTypeCashtag()
