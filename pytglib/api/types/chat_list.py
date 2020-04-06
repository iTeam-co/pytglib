

from ..utils import Object


class ChatList(Object):
    """
    Describes a list of chats

    No parameters required.
    """
    ID = "chatList"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatListMain or ChatListArchive":
        if q.get("@type"):
            return Object.read(q)
        return ChatList()
