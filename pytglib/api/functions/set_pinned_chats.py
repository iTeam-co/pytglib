

from ..utils import Object


class SetPinnedChats(Object):
    """
    Changes the order of pinned chats 

    Attributes:
        ID (:obj:`str`): ``SetPinnedChats``

    Args:
        chat_list (:class:`telegram.api.types.ChatList`):
            Chat list in which to change the order of pinned chats 
        chat_ids (List of :obj:`int`):
            The new list of pinned chats

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setPinnedChats"

    def __init__(self, chat_list, chat_ids, extra=None, **kwargs):
        self.extra = extra
        self.chat_list = chat_list  # ChatList
        self.chat_ids = chat_ids  # list of int

    @staticmethod
    def read(q: dict, *args) -> "SetPinnedChats":
        chat_list = Object.read(q.get('chat_list'))
        chat_ids = q.get('chat_ids')
        return SetPinnedChats(chat_list, chat_ids)
