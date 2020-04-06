

from ..utils import Object


class GetCreatedPublicChats(Object):
    """
    Returns a list of public chats of the specified type, owned by the user 

    Attributes:
        ID (:obj:`str`): ``GetCreatedPublicChats``

    Args:
        type (:class:`telegram.api.types.PublicChatType`):
            Type of the public chats to return

    Returns:
        Chats

    Raises:
        :class:`telegram.Error`
    """
    ID = "getCreatedPublicChats"

    def __init__(self, type, extra=None, **kwargs):
        self.extra = extra
        self.type = type  # PublicChatType

    @staticmethod
    def read(q: dict, *args) -> "GetCreatedPublicChats":
        type = Object.read(q.get('type'))
        return GetCreatedPublicChats(type)
