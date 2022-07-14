

from ..utils import Object


class ChatInviteLinkMember(Object):
    """
    Describes a chat member joined a chat via an invite link 

    Attributes:
        ID (:obj:`str`): ``ChatInviteLinkMember``

    Args:
        user_id (:obj:`int`):
            User identifier 
        joined_chat_date (:obj:`int`):
            Point in time (Unix timestamp) when the user joined the chat 
        approver_user_id (:obj:`int`):
            User identifier of the chat administrator, approved user join request

    Returns:
        ChatInviteLinkMember

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatInviteLinkMember"

    def __init__(self, user_id, joined_chat_date, approver_user_id, **kwargs):
        
        self.user_id = user_id  # int
        self.joined_chat_date = joined_chat_date  # int
        self.approver_user_id = approver_user_id  # int

    @staticmethod
    def read(q: dict, *args) -> "ChatInviteLinkMember":
        user_id = q.get('user_id')
        joined_chat_date = q.get('joined_chat_date')
        approver_user_id = q.get('approver_user_id')
        return ChatInviteLinkMember(user_id, joined_chat_date, approver_user_id)
