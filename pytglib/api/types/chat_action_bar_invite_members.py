

from ..utils import Object


class ChatActionBarInviteMembers(Object):
    """
    The chat is a recently created group chat to which new members can be invited

    Attributes:
        ID (:obj:`str`): ``ChatActionBarInviteMembers``

    No parameters required.

    Returns:
        ChatActionBar

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatActionBarInviteMembers"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatActionBarInviteMembers":
        
        return ChatActionBarInviteMembers()
