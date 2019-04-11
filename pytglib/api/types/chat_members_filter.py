

from ..utils import Object


class ChatMembersFilter(Object):
    """
    Specifies the kind of chat members to return in searchChatMembers

    No parameters required.
    """
    ID = "chatMembersFilter"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatMembersFilterBanned or ChatMembersFilterMembers or ChatMembersFilterRestricted or ChatMembersFilterAdministrators or ChatMembersFilterBots":
        if q.get("@type"):
            return Object.read(q)
        return ChatMembersFilter()
