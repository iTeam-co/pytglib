

from ..utils import Object


class RemoveRecentlyFoundChat(Object):
    """
    Removes a chat from the list of recently found chats 

    Attributes:
        ID (:obj:`str`): ``RemoveRecentlyFoundChat``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat to be removed

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "removeRecentlyFoundChat"

    def __init__(self, chat_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int

    @staticmethod
    def read(q: dict, *args) -> "RemoveRecentlyFoundChat":
        chat_id = q.get('chat_id')
        return RemoveRecentlyFoundChat(chat_id)
