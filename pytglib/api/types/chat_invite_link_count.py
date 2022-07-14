

from ..utils import Object


class ChatInviteLinkCount(Object):
    """
    Describes a chat administrator with a number of active and revoked chat invite links

    Attributes:
        ID (:obj:`str`): ``ChatInviteLinkCount``

    Args:
        user_id (:obj:`int`):
            Administrator's user identifier
        invite_link_count (:obj:`int`):
            Number of active invite links
        revoked_invite_link_count (:obj:`int`):
            Number of revoked invite links

    Returns:
        ChatInviteLinkCount

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatInviteLinkCount"

    def __init__(self, user_id, invite_link_count, revoked_invite_link_count, **kwargs):
        
        self.user_id = user_id  # int
        self.invite_link_count = invite_link_count  # int
        self.revoked_invite_link_count = revoked_invite_link_count  # int

    @staticmethod
    def read(q: dict, *args) -> "ChatInviteLinkCount":
        user_id = q.get('user_id')
        invite_link_count = q.get('invite_link_count')
        revoked_invite_link_count = q.get('revoked_invite_link_count')
        return ChatInviteLinkCount(user_id, invite_link_count, revoked_invite_link_count)
