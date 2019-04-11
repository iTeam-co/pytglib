

from ..utils import Object


class ChatTypePrivate(Object):
    """
    An ordinary chat with a user 

    Attributes:
        ID (:obj:`str`): ``ChatTypePrivate``

    Args:
        user_id (:obj:`int`):
            User identifier

    Returns:
        ChatType

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatTypePrivate"

    def __init__(self, user_id, **kwargs):
        
        self.user_id = user_id  # int

    @staticmethod
    def read(q: dict, *args) -> "ChatTypePrivate":
        user_id = q.get('user_id')
        return ChatTypePrivate(user_id)
