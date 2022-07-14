

from ..utils import Object


class RevokeChatInviteLink(Object):
    """
    Revokes invite link for a chat. Available for basic groups, supergroups, and channels. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links.If a primary link is revoked, then additionally to the revoked link returns new primary link

    Attributes:
        ID (:obj:`str`): ``RevokeChatInviteLink``

    Args:
        chat_id (:obj:`int`):
            Chat identifier
        invite_link (:obj:`str`):
            Invite link to be revoked

    Returns:
        ChatInviteLinks

    Raises:
        :class:`telegram.Error`
    """
    ID = "revokeChatInviteLink"

    def __init__(self, chat_id, invite_link, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.invite_link = invite_link  # str

    @staticmethod
    def read(q: dict, *args) -> "RevokeChatInviteLink":
        chat_id = q.get('chat_id')
        invite_link = q.get('invite_link')
        return RevokeChatInviteLink(chat_id, invite_link)
