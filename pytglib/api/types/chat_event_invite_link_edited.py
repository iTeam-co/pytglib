

from ..utils import Object


class ChatEventInviteLinkEdited(Object):
    """
    A chat invite link was edited 

    Attributes:
        ID (:obj:`str`): ``ChatEventInviteLinkEdited``

    Args:
        old_invite_link (:class:`telegram.api.types.chatInviteLink`):
            Previous information about the invite link 
        new_invite_link (:class:`telegram.api.types.chatInviteLink`):
            New information about the invite link

    Returns:
        ChatEventAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatEventInviteLinkEdited"

    def __init__(self, old_invite_link, new_invite_link, **kwargs):
        
        self.old_invite_link = old_invite_link  # ChatInviteLink
        self.new_invite_link = new_invite_link  # ChatInviteLink

    @staticmethod
    def read(q: dict, *args) -> "ChatEventInviteLinkEdited":
        old_invite_link = Object.read(q.get('old_invite_link'))
        new_invite_link = Object.read(q.get('new_invite_link'))
        return ChatEventInviteLinkEdited(old_invite_link, new_invite_link)
