

from ..utils import Object


class GetChats(Object):
    """
    Returns an ordered list of chats from the beginning of a chat list. For informational purposes only. Use loadChats and updates processing instead to maintain chat lists in a consistent state

    Attributes:
        ID (:obj:`str`): ``GetChats``

    Args:
        chat_list (:class:`telegram.api.types.ChatList`):
            The chat list in which to return chats; pass null to get chats from the main chat list 
        limit (:obj:`int`):
            The maximum number of chats to be returned

    Returns:
        Chats

    Raises:
        :class:`telegram.Error`
    """
    ID = "getChats"

    def __init__(self, chat_list, limit, extra=None, **kwargs):
        self.extra = extra
        self.chat_list = chat_list  # ChatList
        self.limit = limit  # int

    @staticmethod
    def read(q: dict, *args) -> "GetChats":
        chat_list = Object.read(q.get('chat_list'))
        limit = q.get('limit')
        return GetChats(chat_list, limit)
