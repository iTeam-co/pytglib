

from ..utils import Object


class ChatListArchive(Object):
    """
    A list of chats usually located at the top of the main chat list. Unmuted chats are automatically moved from the Archive to the Main chat list when a new message arrives

    Attributes:
        ID (:obj:`str`): ``ChatListArchive``

    No parameters required.

    Returns:
        ChatList

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatListArchive"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatListArchive":
        
        return ChatListArchive()
