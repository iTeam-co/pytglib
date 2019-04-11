

from ..utils import Object


class ChatTypeSecret(Object):
    """
    A secret chat with a user 

    Attributes:
        ID (:obj:`str`): ``ChatTypeSecret``

    Args:
        secret_chat_id (:obj:`int`):
            Secret chat identifier 
        user_id (:obj:`int`):
            User identifier of the secret chat peer

    Returns:
        ChatType

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatTypeSecret"

    def __init__(self, secret_chat_id, user_id, **kwargs):
        
        self.secret_chat_id = secret_chat_id  # int
        self.user_id = user_id  # int

    @staticmethod
    def read(q: dict, *args) -> "ChatTypeSecret":
        secret_chat_id = q.get('secret_chat_id')
        user_id = q.get('user_id')
        return ChatTypeSecret(secret_chat_id, user_id)
