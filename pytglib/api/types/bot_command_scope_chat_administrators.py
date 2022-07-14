

from ..utils import Object


class BotCommandScopeChatAdministrators(Object):
    """
    A scope covering all administrators of a chat 

    Attributes:
        ID (:obj:`str`): ``BotCommandScopeChatAdministrators``

    Args:
        chat_id (:obj:`int`):
            Chat identifier

    Returns:
        BotCommandScope

    Raises:
        :class:`telegram.Error`
    """
    ID = "botCommandScopeChatAdministrators"

    def __init__(self, chat_id, **kwargs):
        
        self.chat_id = chat_id  # int

    @staticmethod
    def read(q: dict, *args) -> "BotCommandScopeChatAdministrators":
        chat_id = q.get('chat_id')
        return BotCommandScopeChatAdministrators(chat_id)
