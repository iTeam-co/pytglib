

from ..utils import Object


class ReadAllChatReactions(Object):
    """
    Marks all reactions in a chat as read 

    Attributes:
        ID (:obj:`str`): ``ReadAllChatReactions``

    Args:
        chat_id (:obj:`int`):
            Chat identifier

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "readAllChatReactions"

    def __init__(self, chat_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int

    @staticmethod
    def read(q: dict, *args) -> "ReadAllChatReactions":
        chat_id = q.get('chat_id')
        return ReadAllChatReactions(chat_id)
