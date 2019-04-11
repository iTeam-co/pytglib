

from ..utils import Object


class ReadAllChatMentions(Object):
    """
    Marks all mentions in a chat as read 

    Attributes:
        ID (:obj:`str`): ``ReadAllChatMentions``

    Args:
        chat_id (:obj:`int`):
            Chat identifier

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "readAllChatMentions"

    def __init__(self, chat_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int

    @staticmethod
    def read(q: dict, *args) -> "ReadAllChatMentions":
        chat_id = q.get('chat_id')
        return ReadAllChatMentions(chat_id)
