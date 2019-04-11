

from ..utils import Object


class CheckChatUsername(Object):
    """
    Checks whether a username can be set for a chat 

    Attributes:
        ID (:obj:`str`): ``CheckChatUsername``

    Args:
        chat_id (:obj:`int`):
            Chat identifier; should be identifier of a supergroup chat, or a channel chat, or a private chat with self, or zero if chat is being created 
        username (:obj:`str`):
            Username to be checked

    Returns:
        CheckChatUsernameResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "checkChatUsername"

    def __init__(self, chat_id, username, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.username = username  # str

    @staticmethod
    def read(q: dict, *args) -> "CheckChatUsername":
        chat_id = q.get('chat_id')
        username = q.get('username')
        return CheckChatUsername(chat_id, username)
