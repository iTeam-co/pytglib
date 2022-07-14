

from ..utils import Object


class InlineKeyboardButtonTypeCallbackWithPassword(Object):
    """
    A button that asks for password of the current user and then sends a callback query to a bot 

    Attributes:
        ID (:obj:`str`): ``InlineKeyboardButtonTypeCallbackWithPassword``

    Args:
        data (:obj:`bytes`):
            Data to be sent to the bot via a callback query

    Returns:
        InlineKeyboardButtonType

    Raises:
        :class:`telegram.Error`
    """
    ID = "inlineKeyboardButtonTypeCallbackWithPassword"

    def __init__(self, data, **kwargs):
        
        self.data = data  # bytes

    @staticmethod
    def read(q: dict, *args) -> "InlineKeyboardButtonTypeCallbackWithPassword":
        data = q.get('data')
        return InlineKeyboardButtonTypeCallbackWithPassword(data)
