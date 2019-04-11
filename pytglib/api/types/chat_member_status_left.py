

from ..utils import Object


class ChatMemberStatusLeft(Object):
    """
    The user is not a chat member

    Attributes:
        ID (:obj:`str`): ``ChatMemberStatusLeft``

    No parameters required.

    Returns:
        ChatMemberStatus

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatMemberStatusLeft"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatMemberStatusLeft":
        
        return ChatMemberStatusLeft()
