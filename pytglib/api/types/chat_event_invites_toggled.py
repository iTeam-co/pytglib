

from ..utils import Object


class ChatEventInvitesToggled(Object):
    """
    The anyone_can_invite setting of a supergroup chat was toggled 

    Attributes:
        ID (:obj:`str`): ``ChatEventInvitesToggled``

    Args:
        anyone_can_invite (:obj:`bool`):
            New value of anyone_can_invite

    Returns:
        ChatEventAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatEventInvitesToggled"

    def __init__(self, anyone_can_invite, **kwargs):
        
        self.anyone_can_invite = anyone_can_invite  # bool

    @staticmethod
    def read(q: dict, *args) -> "ChatEventInvitesToggled":
        anyone_can_invite = q.get('anyone_can_invite')
        return ChatEventInvitesToggled(anyone_can_invite)
