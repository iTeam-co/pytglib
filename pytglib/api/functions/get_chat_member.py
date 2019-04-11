

from ..utils import Object


class GetChatMember(Object):
    """
    Returns information about a single member of a chat 

    Attributes:
        ID (:obj:`str`): ``GetChatMember``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        user_id (:obj:`int`):
            User identifier

    Returns:
        ChatMember

    Raises:
        :class:`telegram.Error`
    """
    ID = "getChatMember"

    def __init__(self, chat_id, user_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.user_id = user_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetChatMember":
        chat_id = q.get('chat_id')
        user_id = q.get('user_id')
        return GetChatMember(chat_id, user_id)
