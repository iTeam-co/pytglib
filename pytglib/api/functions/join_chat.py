

from ..utils import Object


class JoinChat(Object):
    """
    Adds current user as a new member to a chat. Private and secret chats can't be joined using this method 

    Attributes:
        ID (:obj:`str`): ``JoinChat``

    Args:
        chat_id (:obj:`int`):
            Chat identifier

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "joinChat"

    def __init__(self, chat_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int

    @staticmethod
    def read(q: dict, *args) -> "JoinChat":
        chat_id = q.get('chat_id')
        return JoinChat(chat_id)
