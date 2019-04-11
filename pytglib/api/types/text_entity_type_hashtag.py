

from ..utils import Object


class TextEntityTypeHashtag(Object):
    """
    A hashtag text, beginning with "#"

    Attributes:
        ID (:obj:`str`): ``TextEntityTypeHashtag``

    No parameters required.

    Returns:
        TextEntityType

    Raises:
        :class:`telegram.Error`
    """
    ID = "textEntityTypeHashtag"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "TextEntityTypeHashtag":
        
        return TextEntityTypeHashtag()
