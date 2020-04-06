

from ..utils import Object


class PublicChatType(Object):
    """
    Describes a type of public chats

    No parameters required.
    """
    ID = "publicChatType"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PublicChatTypeHasUsername or PublicChatTypeIsLocationBased":
        if q.get("@type"):
            return Object.read(q)
        return PublicChatType()
