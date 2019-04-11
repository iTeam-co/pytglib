

from ..utils import Object


class InlineKeyboardButtonTypeSwitchInline(Object):
    """
    A button that forces an inline query to the bot to be inserted in the input field 

    Attributes:
        ID (:obj:`str`): ``InlineKeyboardButtonTypeSwitchInline``

    Args:
        query (:obj:`str`):
            Inline query to be sent to the bot 
        in_current_chat (:obj:`bool`):
            True, if the inline query should be sent from the current chat

    Returns:
        InlineKeyboardButtonType

    Raises:
        :class:`telegram.Error`
    """
    ID = "inlineKeyboardButtonTypeSwitchInline"

    def __init__(self, query, in_current_chat, **kwargs):
        
        self.query = query  # str
        self.in_current_chat = in_current_chat  # bool

    @staticmethod
    def read(q: dict, *args) -> "InlineKeyboardButtonTypeSwitchInline":
        query = q.get('query')
        in_current_chat = q.get('in_current_chat')
        return InlineKeyboardButtonTypeSwitchInline(query, in_current_chat)
