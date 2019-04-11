

from ..utils import Object


class RichTextFixed(Object):
    """
    A fixed-width rich text 

    Attributes:
        ID (:obj:`str`): ``RichTextFixed``

    Args:
        text (:class:`telegram.api.types.RichText`):
            Text

    Returns:
        RichText

    Raises:
        :class:`telegram.Error`
    """
    ID = "richTextFixed"

    def __init__(self, text, **kwargs):
        
        self.text = text  # RichText

    @staticmethod
    def read(q: dict, *args) -> "RichTextFixed":
        text = Object.read(q.get('text'))
        return RichTextFixed(text)
