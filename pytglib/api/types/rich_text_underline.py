

from ..utils import Object


class RichTextUnderline(Object):
    """
    An underlined rich text 

    Attributes:
        ID (:obj:`str`): ``RichTextUnderline``

    Args:
        text (:class:`telegram.api.types.RichText`):
            Text

    Returns:
        RichText

    Raises:
        :class:`telegram.Error`
    """
    ID = "richTextUnderline"

    def __init__(self, text, **kwargs):
        
        self.text = text  # RichText

    @staticmethod
    def read(q: dict, *args) -> "RichTextUnderline":
        text = Object.read(q.get('text'))
        return RichTextUnderline(text)
