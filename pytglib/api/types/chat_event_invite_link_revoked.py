

from ..utils import Object


class ChatEventInviteLinkRevoked(Object):
    """
    A chat invite link was revoked 

    Attributes:
        ID (:obj:`str`): ``ChatEventInviteLinkRevoked``

    Args:
        invite_link (:class:`telegram.api.types.chatInviteLink`):
            The invite link

    Returns:
        ChatEventAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatEventInviteLinkRevoked"

    def __init__(self, invite_link, **kwargs):
        
        self.invite_link = invite_link  # ChatInviteLink

    @staticmethod
    def read(q: dict, *args) -> "ChatEventInviteLinkRevoked":
        invite_link = Object.read(q.get('invite_link'))
        return ChatEventInviteLinkRevoked(invite_link)
