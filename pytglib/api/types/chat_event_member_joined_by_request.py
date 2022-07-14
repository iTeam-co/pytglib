

from ..utils import Object


class ChatEventMemberJoinedByRequest(Object):
    """
    A new member was accepted to the chat by an administrator 

    Attributes:
        ID (:obj:`str`): ``ChatEventMemberJoinedByRequest``

    Args:
        approver_user_id (:obj:`int`):
            User identifier of the chat administrator, approved user join request 
        invite_link (:class:`telegram.api.types.chatInviteLink`):
            Invite link used to join the chat; may be null

    Returns:
        ChatEventAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatEventMemberJoinedByRequest"

    def __init__(self, approver_user_id, invite_link, **kwargs):
        
        self.approver_user_id = approver_user_id  # int
        self.invite_link = invite_link  # ChatInviteLink

    @staticmethod
    def read(q: dict, *args) -> "ChatEventMemberJoinedByRequest":
        approver_user_id = q.get('approver_user_id')
        invite_link = Object.read(q.get('invite_link'))
        return ChatEventMemberJoinedByRequest(approver_user_id, invite_link)
