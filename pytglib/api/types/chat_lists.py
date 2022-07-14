

from ..utils import Object


class ChatLists(Object):
    """
    Contains a list of chat lists 

    Attributes:
        ID (:obj:`str`): ``ChatLists``

    Args:
        chat_lists (List of :class:`telegram.api.types.ChatList`):
            List of chat lists

    Returns:
        ChatLists

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatLists"

    def __init__(self, chat_lists, **kwargs):
        
        self.chat_lists = chat_lists  # list of ChatList

    @staticmethod
    def read(q: dict, *args) -> "ChatLists":
        chat_lists = [Object.read(i) for i in q.get('chat_lists', [])]
        return ChatLists(chat_lists)
