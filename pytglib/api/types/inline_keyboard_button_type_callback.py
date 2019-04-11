

from ..utils import Object


class InlineKeyboardButtonTypeCallback(Object):
    """
    A button that sends a special callback query to a bot 

    Attributes:
        ID (:obj:`str`): ``InlineKeyboardButtonTypeCallback``

    Args:
        data (:obj:`bytes`):
            Data to be sent to the bot via a callback query

    Returns:
        InlineKeyboardButtonType

    Raises:
        :class:`telegram.Error`
    """
    ID = "inlineKeyboardButtonTypeCallback"

    def __init__(self, data, **kwargs):
        
        self.data = data  # bytes

    @staticmethod
    def read(q: dict, *args) -> "InlineKeyboardButtonTypeCallback":
        data = q.get('data')
        return InlineKeyboardButtonTypeCallback(data)
