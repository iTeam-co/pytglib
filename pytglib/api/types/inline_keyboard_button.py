

from ..utils import Object


class InlineKeyboardButton(Object):
    """
    Represents a single button in an inline keyboard 

    Attributes:
        ID (:obj:`str`): ``InlineKeyboardButton``

    Args:
        text (:obj:`str`):
            Text of the button 
        type (:class:`telegram.api.types.InlineKeyboardButtonType`):
            Type of the button

    Returns:
        InlineKeyboardButton

    Raises:
        :class:`telegram.Error`
    """
    ID = "inlineKeyboardButton"

    def __init__(self, text, type, **kwargs):
        
        self.text = text  # str
        self.type = type  # InlineKeyboardButtonType

    @staticmethod
    def read(q: dict, *args) -> "InlineKeyboardButton":
        text = q.get('text')
        type = Object.read(q.get('type'))
        return InlineKeyboardButton(text, type)
