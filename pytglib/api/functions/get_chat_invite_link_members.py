

from ..utils import Object


class GetChatInviteLinkMembers(Object):
    """
    Returns chat members joined a chat via an invite link. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links 

    Attributes:
        ID (:obj:`str`): ``GetChatInviteLinkMembers``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        invite_link (:obj:`str`):
            Invite link for which to return chat members
        offset_member (:class:`telegram.api.types.chatInviteLinkMember`):
            A chat member from which to return next chat members; pass null to get results from the beginning 
        limit (:obj:`int`):
            The maximum number of chat members to return; up to 100

    Returns:
        ChatInviteLinkMembers

    Raises:
        :class:`telegram.Error`
    """
    ID = "getChatInviteLinkMembers"

    def __init__(self, chat_id, invite_link, offset_member, limit, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.invite_link = invite_link  # str
        self.offset_member = offset_member  # ChatInviteLinkMember
        self.limit = limit  # int

    @staticmethod
    def read(q: dict, *args) -> "GetChatInviteLinkMembers":
        chat_id = q.get('chat_id')
        invite_link = q.get('invite_link')
        offset_member = Object.read(q.get('offset_member'))
        limit = q.get('limit')
        return GetChatInviteLinkMembers(chat_id, invite_link, offset_member, limit)
