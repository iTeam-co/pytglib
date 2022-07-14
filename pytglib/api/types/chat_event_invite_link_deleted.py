

from ..utils import Object


class ChatEventInviteLinkDeleted(Object):
    """
    A revoked chat invite link was deleted 

    Attributes:
        ID (:obj:`str`): ``ChatEventInviteLinkDeleted``

    Args:
        invite_link (:class:`telegram.api.types.chatInviteLink`):
            The invite link

    Returns:
        ChatEventAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatEventInviteLinkDeleted"

    def __init__(self, invite_link, **kwargs):
        
        self.invite_link = invite_link  # ChatInviteLink

    @staticmethod
    def read(q: dict, *args) -> "ChatEventInviteLinkDeleted":
        invite_link = Object.read(q.get('invite_link'))
        return ChatEventInviteLinkDeleted(invite_link)
