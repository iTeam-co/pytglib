

from ..utils import Object


class RichTextMarked(Object):
    """
    A marked rich text 

    Attributes:
        ID (:obj:`str`): ``RichTextMarked``

    Args:
        text (:class:`telegram.api.types.RichText`):
            Text

    Returns:
        RichText

    Raises:
        :class:`telegram.Error`
    """
    ID = "richTextMarked"

    def __init__(self, text, **kwargs):
        
        self.text = text  # RichText

    @staticmethod
    def read(q: dict, *args) -> "RichTextMarked":
        text = Object.read(q.get('text'))
        return RichTextMarked(text)
