

from ..utils import Object


class ChatListFilter(Object):
    """
    A list of chats belonging to a chat filter 

    Attributes:
        ID (:obj:`str`): ``ChatListFilter``

    Args:
        chat_filter_id (:obj:`int`):
            Chat filter identifier

    Returns:
        ChatList

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatListFilter"

    def __init__(self, chat_filter_id, **kwargs):
        
        self.chat_filter_id = chat_filter_id  # int

    @staticmethod
    def read(q: dict, *args) -> "ChatListFilter":
        chat_filter_id = q.get('chat_filter_id')
        return ChatListFilter(chat_filter_id)
