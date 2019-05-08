

from ..utils import Object


class RichTextAnchor(Object):
    """
    A rich text anchor 

    Attributes:
        ID (:obj:`str`): ``RichTextAnchor``

    Args:
        text (:class:`telegram.api.types.RichText`):
            Text 
        name (:obj:`str`):
            Anchor name

    Returns:
        RichText

    Raises:
        :class:`telegram.Error`
    """
    ID = "richTextAnchor"

    def __init__(self, text, name, **kwargs):
        
        self.text = text  # RichText
        self.name = name  # str

    @staticmethod
    def read(q: dict, *args) -> "RichTextAnchor":
        text = Object.read(q.get('text'))
        name = q.get('name')
        return RichTextAnchor(text, name)
