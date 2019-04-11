

from ..utils import Object


class ChatEventMemberPromoted(Object):
    """
    A chat member has gained/lost administrator status, or the list of their administrator privileges has changed 

    Attributes:
        ID (:obj:`str`): ``ChatEventMemberPromoted``

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
    ID = "chatEventMemberPromoted"

    def __init__(self, user_id, old_status, new_status, **kwargs):
        
        self.user_id = user_id  # int
        self.old_status = old_status  # ChatMemberStatus
        self.new_status = new_status  # ChatMemberStatus

    @staticmethod
    def read(q: dict, *args) -> "ChatEventMemberPromoted":
        user_id = q.get('user_id')
        old_status = Object.read(q.get('old_status'))
        new_status = Object.read(q.get('new_status'))
        return ChatEventMemberPromoted(user_id, old_status, new_status)
