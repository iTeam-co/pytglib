

from ..utils import Object


class RichTextStrikethrough(Object):
    """
    A strikethrough rich text 

    Attributes:
        ID (:obj:`str`): ``RichTextStrikethrough``

    Args:
        text (:class:`telegram.api.types.RichText`):
            Text

    Returns:
        RichText

    Raises:
        :class:`telegram.Error`
    """
    ID = "richTextStrikethrough"

    def __init__(self, text, **kwargs):
        
        self.text = text  # RichText

    @staticmethod
    def read(q: dict, *args) -> "RichTextStrikethrough":
        text = Object.read(q.get('text'))
        return RichTextStrikethrough(text)
