

from ..utils import Object


class EditChatInviteLink(Object):
    """
    Edits a non-primary invite link for a chat. Available for basic groups, supergroups, and channels. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links

    Attributes:
        ID (:obj:`str`): ``EditChatInviteLink``

    Args:
        chat_id (:obj:`int`):
            Chat identifier
        invite_link (:obj:`str`):
            Invite link to be edited
        name (:obj:`str`):
            Invite link name; 0-32 characters
        expiration_date (:obj:`int`):
            Point in time (Unix timestamp) when the link will expire; pass 0 if never
        member_limit (:obj:`int`):
            The maximum number of chat members that can join the chat via the link simultaneously; 0-99999; pass 0 if not limited
        creates_join_request (:obj:`bool`):
            Pass true if users joining the chat via the link need to be approved by chat administratorsIn this case, member_limit must be 0

    Returns:
        ChatInviteLink

    Raises:
        :class:`telegram.Error`
    """
    ID = "editChatInviteLink"

    def __init__(self, chat_id, invite_link, name, expiration_date, member_limit, creates_join_request, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.invite_link = invite_link  # str
        self.name = name  # str
        self.expiration_date = expiration_date  # int
        self.member_limit = member_limit  # int
        self.creates_join_request = creates_join_request  # bool

    @staticmethod
    def read(q: dict, *args) -> "EditChatInviteLink":
        chat_id = q.get('chat_id')
        invite_link = q.get('invite_link')
        name = q.get('name')
        expiration_date = q.get('expiration_date')
        member_limit = q.get('member_limit')
        creates_join_request = q.get('creates_join_request')
        return EditChatInviteLink(chat_id, invite_link, name, expiration_date, member_limit, creates_join_request)
