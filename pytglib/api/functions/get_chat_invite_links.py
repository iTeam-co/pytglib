

from ..utils import Object


class GetChatInviteLinks(Object):
    """
    Returns invite links for a chat created by specified administrator. Requires administrator privileges and can_invite_users right in the chat to get own links and owner privileges to get other links

    Attributes:
        ID (:obj:`str`): ``GetChatInviteLinks``

    Args:
        chat_id (:obj:`int`):
            Chat identifier
        creator_user_id (:obj:`int`):
            User identifier of a chat administratorMust be an identifier of the current user for non-owner
        is_revoked (:obj:`bool`):
            Pass true if revoked links needs to be returned instead of active or expired
        offset_date (:obj:`int`):
            Creation date of an invite link starting after which to return invite links; use 0 to get results from the beginning
        offset_invite_link (:obj:`str`):
            Invite link starting after which to return invite links; use empty string to get results from the beginning
        limit (:obj:`int`):
            The maximum number of invite links to return; up to 100

    Returns:
        ChatInviteLinks

    Raises:
        :class:`telegram.Error`
    """
    ID = "getChatInviteLinks"

    def __init__(self, chat_id, creator_user_id, is_revoked, offset_date, offset_invite_link, limit, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.creator_user_id = creator_user_id  # int
        self.is_revoked = is_revoked  # bool
        self.offset_date = offset_date  # int
        self.offset_invite_link = offset_invite_link  # str
        self.limit = limit  # int

    @staticmethod
    def read(q: dict, *args) -> "GetChatInviteLinks":
        chat_id = q.get('chat_id')
        creator_user_id = q.get('creator_user_id')
        is_revoked = q.get('is_revoked')
        offset_date = q.get('offset_date')
        offset_invite_link = q.get('offset_invite_link')
        limit = q.get('limit')
        return GetChatInviteLinks(chat_id, creator_user_id, is_revoked, offset_date, offset_invite_link, limit)
