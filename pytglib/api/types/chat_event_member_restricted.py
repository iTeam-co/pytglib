

from ..utils import Object


class ChatEventMemberRestricted(Object):
    """
    A chat member was restricted/unrestricted or banned/unbanned, or the list of their restrictions has changed 

    Attributes:
        ID (:obj:`str`): ``ChatEventMemberRestricted``

    Args:
        member_id (:class:`telegram.api.types.MessageSender`):
            Affected chat member identifier 
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

    def __init__(self, member_id, old_status, new_status, **kwargs):
        
        self.member_id = member_id  # MessageSender
        self.old_status = old_status  # ChatMemberStatus
        self.new_status = new_status  # ChatMemberStatus

    @staticmethod
    def read(q: dict, *args) -> "ChatEventMemberRestricted":
        member_id = Object.read(q.get('member_id'))
        old_status = Object.read(q.get('old_status'))
        new_status = Object.read(q.get('new_status'))
        return ChatEventMemberRestricted(member_id, old_status, new_status)
