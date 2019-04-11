

from ..utils import Object


class ChatMemberStatusCreator(Object):
    """
    The user is the creator of a chat and has all the administrator privileges 

    Attributes:
        ID (:obj:`str`): ``ChatMemberStatusCreator``

    Args:
        is_member (:obj:`bool`):
            True, if the user is a member of the chat

    Returns:
        ChatMemberStatus

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatMemberStatusCreator"

    def __init__(self, is_member, **kwargs):
        
        self.is_member = is_member  # bool

    @staticmethod
    def read(q: dict, *args) -> "ChatMemberStatusCreator":
        is_member = q.get('is_member')
        return ChatMemberStatusCreator(is_member)
