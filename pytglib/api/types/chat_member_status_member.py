

from ..utils import Object


class ChatMemberStatusMember(Object):
    """
    The user is a member of a chat, without any additional privileges or restrictions

    Attributes:
        ID (:obj:`str`): ``ChatMemberStatusMember``

    No parameters required.

    Returns:
        ChatMemberStatus

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatMemberStatusMember"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatMemberStatusMember":
        
        return ChatMemberStatusMember()
