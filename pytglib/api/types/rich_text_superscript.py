

from ..utils import Object


class RichTextSuperscript(Object):
    """
    A superscript rich text 

    Attributes:
        ID (:obj:`str`): ``RichTextSuperscript``

    Args:
        text (:class:`telegram.api.types.RichText`):
            Text

    Returns:
        RichText

    Raises:
        :class:`telegram.Error`
    """
    ID = "richTextSuperscript"

    def __init__(self, text, **kwargs):
        
        self.text = text  # RichText

    @staticmethod
    def read(q: dict, *args) -> "RichTextSuperscript":
        text = Object.read(q.get('text'))
        return RichTextSuperscript(text)
