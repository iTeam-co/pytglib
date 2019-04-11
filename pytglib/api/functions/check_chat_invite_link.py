

from ..utils import Object


class CheckChatInviteLink(Object):
    """
    Checks the validity of an invite link for a chat and returns information about the corresponding chat 

    Attributes:
        ID (:obj:`str`): ``CheckChatInviteLink``

    Args:
        invite_link (:obj:`str`):
            Invite link to be checked; should begin with "https://tme/joinchat/", "https://telegramme/joinchat/", or "https://telegramdog/joinchat/"

    Returns:
        ChatInviteLinkInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "checkChatInviteLink"

    def __init__(self, invite_link, extra=None, **kwargs):
        self.extra = extra
        self.invite_link = invite_link  # str

    @staticmethod
    def read(q: dict, *args) -> "CheckChatInviteLink":
        invite_link = q.get('invite_link')
        return CheckChatInviteLink(invite_link)
