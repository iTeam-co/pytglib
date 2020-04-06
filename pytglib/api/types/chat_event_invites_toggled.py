

from ..utils import Object


class ChatEventInvitesToggled(Object):
    """
    The can_invite_users permission of a supergroup chat was toggled 

    Attributes:
        ID (:obj:`str`): ``ChatEventInvitesToggled``

    Args:
        can_invite_users (:obj:`bool`):
            New value of can_invite_users permission

    Returns:
        ChatEventAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatEventInvitesToggled"

    def __init__(self, can_invite_users, **kwargs):
        
        self.can_invite_users = can_invite_users  # bool

    @staticmethod
    def read(q: dict, *args) -> "ChatEventInvitesToggled":
        can_invite_users = q.get('can_invite_users')
        return ChatEventInvitesToggled(can_invite_users)
