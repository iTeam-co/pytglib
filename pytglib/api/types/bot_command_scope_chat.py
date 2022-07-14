

from ..utils import Object


class BotCommandScopeChat(Object):
    """
    A scope covering all members of a chat 

    Attributes:
        ID (:obj:`str`): ``BotCommandScopeChat``

    Args:
        chat_id (:obj:`int`):
            Chat identifier

    Returns:
        BotCommandScope

    Raises:
        :class:`telegram.Error`
    """
    ID = "botCommandScopeChat"

    def __init__(self, chat_id, **kwargs):
        
        self.chat_id = chat_id  # int

    @staticmethod
    def read(q: dict, *args) -> "BotCommandScopeChat":
        chat_id = q.get('chat_id')
        return BotCommandScopeChat(chat_id)
