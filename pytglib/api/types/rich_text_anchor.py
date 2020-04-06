

from ..utils import Object


class RichTextAnchor(Object):
    """
    An anchor 

    Attributes:
        ID (:obj:`str`): ``RichTextAnchor``

    Args:
        name (:obj:`str`):
            Anchor name

    Returns:
        RichText

    Raises:
        :class:`telegram.Error`
    """
    ID = "richTextAnchor"

    def __init__(self, name, **kwargs):
        
        self.name = name  # str

    @staticmethod
    def read(q: dict, *args) -> "RichTextAnchor":
        name = q.get('name')
        return RichTextAnchor(name)
