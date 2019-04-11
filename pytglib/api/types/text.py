

from ..utils import Object


class Text(Object):
    """
    Contains some text 

    Attributes:
        ID (:obj:`str`): ``Text``

    Args:
        text (:obj:`str`):
            Text

    Returns:
        Text

    Raises:
        :class:`telegram.Error`
    """
    ID = "text"

    def __init__(self, text, **kwargs):
        
        self.text = text  # str

    @staticmethod
    def read(q: dict, *args) -> "Text":
        text = q.get('text')
        return Text(text)
