

from ..utils import Object


class AddRecentlyFoundChat(Object):
    """
    Adds a chat to the list of recently found chats. The chat is added to the beginning of the list. If the chat is already in the list, it will be removed from the list first 

    Attributes:
        ID (:obj:`str`): ``AddRecentlyFoundChat``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat to add

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "addRecentlyFoundChat"

    def __init__(self, chat_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int

    @staticmethod
    def read(q: dict, *args) -> "AddRecentlyFoundChat":
        chat_id = q.get('chat_id')
        return AddRecentlyFoundChat(chat_id)
