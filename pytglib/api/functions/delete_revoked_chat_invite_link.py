

from ..utils import Object


class DeleteRevokedChatInviteLink(Object):
    """
    Deletes revoked chat invite links. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links 

    Attributes:
        ID (:obj:`str`): ``DeleteRevokedChatInviteLink``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        invite_link (:obj:`str`):
            Invite link to revoke

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "deleteRevokedChatInviteLink"

    def __init__(self, chat_id, invite_link, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.invite_link = invite_link  # str

    @staticmethod
    def read(q: dict, *args) -> "DeleteRevokedChatInviteLink":
        chat_id = q.get('chat_id')
        invite_link = q.get('invite_link')
        return DeleteRevokedChatInviteLink(chat_id, invite_link)
