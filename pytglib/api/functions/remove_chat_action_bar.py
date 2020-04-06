

from ..utils import Object


class RemoveChatActionBar(Object):
    """
    Removes a chat action bar without any other action 

    Attributes:
        ID (:obj:`str`): ``RemoveChatActionBar``

    Args:
        chat_id (:obj:`int`):
            Chat identifier

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "removeChatActionBar"

    def __init__(self, chat_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int

    @staticmethod
    def read(q: dict, *args) -> "RemoveChatActionBar":
        chat_id = q.get('chat_id')
        return RemoveChatActionBar(chat_id)
