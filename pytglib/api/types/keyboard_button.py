

from ..utils import Object


class KeyboardButton(Object):
    """
    Represents a single button in a bot keyboard 

    Attributes:
        ID (:obj:`str`): ``KeyboardButton``

    Args:
        text (:obj:`str`):
            Text of the button 
        type (:class:`telegram.api.types.KeyboardButtonType`):
            Type of the button

    Returns:
        KeyboardButton

    Raises:
        :class:`telegram.Error`
    """
    ID = "keyboardButton"

    def __init__(self, text, type, **kwargs):
        
        self.text = text  # str
        self.type = type  # KeyboardButtonType

    @staticmethod
    def read(q: dict, *args) -> "KeyboardButton":
        text = q.get('text')
        type = Object.read(q.get('type'))
        return KeyboardButton(text, type)
