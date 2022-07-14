

from ..utils import Object


class ChatMember(Object):
    """
    Describes a user or a chat as a member of another chat

    Attributes:
        ID (:obj:`str`): ``ChatMember``

    Args:
        member_id (:class:`telegram.api.types.MessageSender`):
            Identifier of the chat memberCurrently, other chats can be only Left or BannedOnly supergroups and channels can have other chats as Left or Banned members and these chats must be supergroups or channels
        inviter_user_id (:obj:`int`):
            Identifier of a user that invited/promoted/banned this member in the chat; 0 if unknown
        joined_chat_date (:obj:`int`):
            Point in time (Unix timestamp) when the user joined the chat
        status (:class:`telegram.api.types.ChatMemberStatus`):
            Status of the member in the chat

    Returns:
        ChatMember

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatMember"

    def __init__(self, member_id, inviter_user_id, joined_chat_date, status, **kwargs):
        
        self.member_id = member_id  # MessageSender
        self.inviter_user_id = inviter_user_id  # int
        self.joined_chat_date = joined_chat_date  # int
        self.status = status  # ChatMemberStatus

    @staticmethod
    def read(q: dict, *args) -> "ChatMember":
        member_id = Object.read(q.get('member_id'))
        inviter_user_id = q.get('inviter_user_id')
        joined_chat_date = q.get('joined_chat_date')
        status = Object.read(q.get('status'))
        return ChatMember(member_id, inviter_user_id, joined_chat_date, status)
