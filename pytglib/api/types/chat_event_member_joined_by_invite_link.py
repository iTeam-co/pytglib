

from ..utils import Object


class ChatEventMemberJoinedByInviteLink(Object):
    """
    A new member joined the chat via an invite link 

    Attributes:
        ID (:obj:`str`): ``ChatEventMemberJoinedByInviteLink``

    Args:
        invite_link (:class:`telegram.api.types.chatInviteLink`):
            Invite link used to join the chat

    Returns:
        ChatEventAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatEventMemberJoinedByInviteLink"

    def __init__(self, invite_link, **kwargs):
        
        self.invite_link = invite_link  # ChatInviteLink

    @staticmethod
    def read(q: dict, *args) -> "ChatEventMemberJoinedByInviteLink":
        invite_link = Object.read(q.get('invite_link'))
        return ChatEventMemberJoinedByInviteLink(invite_link)
