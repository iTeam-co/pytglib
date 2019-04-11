

from ..utils import Object


class ChatEventMemberRestricted(Object):
    """
    A chat member was restricted/unrestricted or banned/unbanned, or the list of their restrictions has changed 

    Attributes:
        ID (:obj:`str`): ``ChatEventMemberRestricted``

    Args:
        user_id (:obj:`int`):
            Chat member user identifier 
        old_status (:class:`telegram.api.types.ChatMemberStatus`):
            Previous status of the chat member 
        new_status (:class:`telegram.api.types.ChatMemberStatus`):
            New status of the chat member

    Returns:
        ChatEventAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatEventMemberRestricted"

    def __init__(self, user_id, old_status, new_status, **kwargs):
        
        self.user_id = user_id  # int
        self.old_status = old_status  # ChatMemberStatus
        self.new_status = new_status  # ChatMemberStatus

    @staticmethod
    def read(q: dict, *args) -> "ChatEventMemberRestricted":
        user_id = q.get('user_id')
        old_status = Object.read(q.get('old_status'))
        new_status = Object.read(q.get('new_status'))
        return ChatEventMemberRestricted(user_id, old_status, new_status)
