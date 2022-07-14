

from ..utils import Object


class BotCommandScopeChatMember(Object):
    """
    A scope covering a member of a chat 

    Attributes:
        ID (:obj:`str`): ``BotCommandScopeChatMember``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        user_id (:obj:`int`):
            User identifier

    Returns:
        BotCommandScope

    Raises:
        :class:`telegram.Error`
    """
    ID = "botCommandScopeChatMember"

    def __init__(self, chat_id, user_id, **kwargs):
        
        self.chat_id = chat_id  # int
        self.user_id = user_id  # int

    @staticmethod
    def read(q: dict, *args) -> "BotCommandScopeChatMember":
        chat_id = q.get('chat_id')
        user_id = q.get('user_id')
        return BotCommandScopeChatMember(chat_id, user_id)
