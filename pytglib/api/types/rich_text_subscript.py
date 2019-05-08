

from ..utils import Object


class RichTextSubscript(Object):
    """
    A subscript rich text 

    Attributes:
        ID (:obj:`str`): ``RichTextSubscript``

    Args:
        text (:class:`telegram.api.types.RichText`):
            Text

    Returns:
        RichText

    Raises:
        :class:`telegram.Error`
    """
    ID = "richTextSubscript"

    def __init__(self, text, **kwargs):
        
        self.text = text  # RichText

    @staticmethod
    def read(q: dict, *args) -> "RichTextSubscript":
        text = Object.read(q.get('text'))
        return RichTextSubscript(text)
