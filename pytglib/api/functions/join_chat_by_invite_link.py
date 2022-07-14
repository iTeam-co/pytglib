

from ..utils import Object


class JoinChatByInviteLink(Object):
    """
    Uses an invite link to add the current user to the chat if possible. May return an error with a message "INVITE_REQUEST_SENT" if only a join request was created 

    Attributes:
        ID (:obj:`str`): ``JoinChatByInviteLink``

    Args:
        invite_link (:obj:`str`):
            Invite link to use

    Returns:
        Chat

    Raises:
        :class:`telegram.Error`
    """
    ID = "joinChatByInviteLink"

    def __init__(self, invite_link, extra=None, **kwargs):
        self.extra = extra
        self.invite_link = invite_link  # str

    @staticmethod
    def read(q: dict, *args) -> "JoinChatByInviteLink":
        invite_link = q.get('invite_link')
        return JoinChatByInviteLink(invite_link)
