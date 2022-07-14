

from ..utils import Object


class ChatSource(Object):
    """
    Describes a reason why an external chat is shown in a chat list

    No parameters required.
    """
    ID = "chatSource"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatSourcePublicServiceAnnouncement or ChatSourceMtprotoProxy":
        if q.get("@type"):
            return Object.read(q)
        return ChatSource()
