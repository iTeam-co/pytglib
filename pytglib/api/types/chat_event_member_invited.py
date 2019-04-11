

from ..utils import Object


class ChatEventMemberInvited(Object):
    """
    A new chat member was invited 

    Attributes:
        ID (:obj:`str`): ``ChatEventMemberInvited``

    Args:
        user_id (:obj:`int`):
            New member user identifier 
        status (:class:`telegram.api.types.ChatMemberStatus`):
            New member status

    Returns:
        ChatEventAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatEventMemberInvited"

    def __init__(self, user_id, status, **kwargs):
        
        self.user_id = user_id  # int
        self.status = status  # ChatMemberStatus

    @staticmethod
    def read(q: dict, *args) -> "ChatEventMemberInvited":
        user_id = q.get('user_id')
        status = Object.read(q.get('status'))
        return ChatEventMemberInvited(user_id, status)
