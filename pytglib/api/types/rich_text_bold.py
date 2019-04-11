

from ..utils import Object


class RichTextBold(Object):
    """
    A bold rich text 

    Attributes:
        ID (:obj:`str`): ``RichTextBold``

    Args:
        text (:class:`telegram.api.types.RichText`):
            Text

    Returns:
        RichText

    Raises:
        :class:`telegram.Error`
    """
    ID = "richTextBold"

    def __init__(self, text, **kwargs):
        
        self.text = text  # RichText

    @staticmethod
    def read(q: dict, *args) -> "RichTextBold":
        text = Object.read(q.get('text'))
        return RichTextBold(text)
