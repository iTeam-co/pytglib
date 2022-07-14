

from ..utils import Object


class ChatInviteLink(Object):
    """
    Contains a chat invite link

    Attributes:
        ID (:obj:`str`): ``ChatInviteLink``

    Args:
        invite_link (:obj:`str`):
            Chat invite link
        name (:obj:`str`):
            Name of the link
        creator_user_id (:obj:`int`):
            User identifier of an administrator created the link
        date (:obj:`int`):
            Point in time (Unix timestamp) when the link was created
        edit_date (:obj:`int`):
            Point in time (Unix timestamp) when the link was last edited; 0 if never or unknown
        expiration_date (:obj:`int`):
            Point in time (Unix timestamp) when the link will expire; 0 if never
        member_limit (:obj:`int`):
            The maximum number of members, which can join the chat using the link simultaneously; 0 if not limitedAlways 0 if the link requires approval
        member_count (:obj:`int`):
            Number of chat members, which joined the chat using the link
        pending_join_request_count (:obj:`int`):
            Number of pending join requests created using this link
        creates_join_request (:obj:`bool`):
            True, if the link only creates join requestIf true, total number of joining members will be unlimited
        is_primary (:obj:`bool`):
            True, if the link is primaryPrimary invite link can't have name, expiration date, or usage limitThere is exactly one primary invite link for each administrator with can_invite_users right at a given time
        is_revoked (:obj:`bool`):
            True, if the link was revoked

    Returns:
        ChatInviteLink

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatInviteLink"

    def __init__(self, invite_link, name, creator_user_id, date, edit_date, expiration_date, member_limit, member_count, pending_join_request_count, creates_join_request, is_primary, is_revoked, **kwargs):
        
        self.invite_link = invite_link  # str
        self.name = name  # str
        self.creator_user_id = creator_user_id  # int
        self.date = date  # int
        self.edit_date = edit_date  # int
        self.expiration_date = expiration_date  # int
        self.member_limit = member_limit  # int
        self.member_count = member_count  # int
        self.pending_join_request_count = pending_join_request_count  # int
        self.creates_join_request = creates_join_request  # bool
        self.is_primary = is_primary  # bool
        self.is_revoked = is_revoked  # bool

    @staticmethod
    def read(q: dict, *args) -> "ChatInviteLink":
        invite_link = q.get('invite_link')
        name = q.get('name')
        creator_user_id = q.get('creator_user_id')
        date = q.get('date')
        edit_date = q.get('edit_date')
        expiration_date = q.get('expiration_date')
        member_limit = q.get('member_limit')
        member_count = q.get('member_count')
        pending_join_request_count = q.get('pending_join_request_count')
        creates_join_request = q.get('creates_join_request')
        is_primary = q.get('is_primary')
        is_revoked = q.get('is_revoked')
        return ChatInviteLink(invite_link, name, creator_user_id, date, edit_date, expiration_date, member_limit, member_count, pending_join_request_count, creates_join_request, is_primary, is_revoked)
