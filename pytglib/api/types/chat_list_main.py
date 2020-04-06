

from ..utils import Object


class ChatListMain(Object):
    """
    A main list of chats

    Attributes:
        ID (:obj:`str`): ``ChatListMain``

    No parameters required.

    Returns:
        ChatList

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatListMain"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatListMain":
        
        return ChatListMain()
