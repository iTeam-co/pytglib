

from ..utils import Object


class ChatMemberStatus(Object):
    """
    Provides information about the status of a member in a chat

    No parameters required.
    """
    ID = "chatMemberStatus"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatMemberStatusAdministrator or ChatMemberStatusRestricted or ChatMemberStatusLeft or ChatMemberStatusMember or ChatMemberStatusCreator or ChatMemberStatusBanned":
        if q.get("@type"):
            return Object.read(q)
        return ChatMemberStatus()
