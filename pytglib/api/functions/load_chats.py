

from ..utils import Object


class LoadChats(Object):
    """
    Loads more chats from a chat list. The loaded chats and their positions in the chat list will be sent through updates. Chats are sorted by the pair (chat.position.order, chat.id) in descending order. Returns a 404 error if all chats have been loaded

    Attributes:
        ID (:obj:`str`): ``LoadChats``

    Args:
        chat_list (:class:`telegram.api.types.ChatList`):
            The chat list in which to load chats; pass null to load chats from the main chat list
        limit (:obj:`int`):
            The maximum number of chats to be loadedFor optimal performance, the number of loaded chats is chosen by TDLib and can be smaller than the specified limit, even if the end of the list is not reached

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "loadChats"

    def __init__(self, chat_list, limit, extra=None, **kwargs):
        self.extra = extra
        self.chat_list = chat_list  # ChatList
        self.limit = limit  # int

    @staticmethod
    def read(q: dict, *args) -> "LoadChats":
        chat_list = Object.read(q.get('chat_list'))
        limit = q.get('limit')
        return LoadChats(chat_list, limit)
