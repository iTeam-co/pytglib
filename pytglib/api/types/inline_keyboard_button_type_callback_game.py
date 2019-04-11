

from ..utils import Object


class InlineKeyboardButtonTypeCallbackGame(Object):
    """
    A button with a game that sends a special callback query to a bot. This button must be in the first column and row of the keyboard and can be attached only to a message with content of the type messageGame

    Attributes:
        ID (:obj:`str`): ``InlineKeyboardButtonTypeCallbackGame``

    No parameters required.

    Returns:
        InlineKeyboardButtonType

    Raises:
        :class:`telegram.Error`
    """
    ID = "inlineKeyboardButtonTypeCallbackGame"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "InlineKeyboardButtonTypeCallbackGame":
        
        return InlineKeyboardButtonTypeCallbackGame()
