

from ..utils import Object


class RichTextPlain(Object):
    """
    A plain text 

    Attributes:
        ID (:obj:`str`): ``RichTextPlain``

    Args:
        text (:obj:`str`):
            Text

    Returns:
        RichText

    Raises:
        :class:`telegram.Error`
    """
    ID = "richTextPlain"

    def __init__(self, text, **kwargs):
        
        self.text = text  # str

    @staticmethod
    def read(q: dict, *args) -> "RichTextPlain":
        text = q.get('text')
        return RichTextPlain(text)
