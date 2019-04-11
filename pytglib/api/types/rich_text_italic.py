

from ..utils import Object


class RichTextItalic(Object):
    """
    An italicized rich text 

    Attributes:
        ID (:obj:`str`): ``RichTextItalic``

    Args:
        text (:class:`telegram.api.types.RichText`):
            Text

    Returns:
        RichText

    Raises:
        :class:`telegram.Error`
    """
    ID = "richTextItalic"

    def __init__(self, text, **kwargs):
        
        self.text = text  # RichText

    @staticmethod
    def read(q: dict, *args) -> "RichTextItalic":
        text = Object.read(q.get('text'))
        return RichTextItalic(text)
