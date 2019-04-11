

from ..utils import Object


class ChatInviteLink(Object):
    """
    Contains a chat invite link 

    Attributes:
        ID (:obj:`str`): ``ChatInviteLink``

    Args:
        invite_link (:obj:`str`):
            Chat invite link

    Returns:
        ChatInviteLink

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatInviteLink"

    def __init__(self, invite_link, **kwargs):
        
        self.invite_link = invite_link  # str

    @staticmethod
    def read(q: dict, *args) -> "ChatInviteLink":
        invite_link = q.get('invite_link')
        return ChatInviteLink(invite_link)
