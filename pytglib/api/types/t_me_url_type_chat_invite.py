

from ..utils import Object


class TMeUrlTypeChatInvite(Object):
    """
    A chat invite link 

    Attributes:
        ID (:obj:`str`): ``TMeUrlTypeChatInvite``

    Args:
        info (:class:`telegram.api.types.chatInviteLinkInfo`):
            Chat invite link info

    Returns:
        TMeUrlType

    Raises:
        :class:`telegram.Error`
    """
    ID = "tMeUrlTypeChatInvite"

    def __init__(self, info, **kwargs):
        
        self.info = info  # ChatInviteLinkInfo

    @staticmethod
    def read(q: dict, *args) -> "TMeUrlTypeChatInvite":
        info = Object.read(q.get('info'))
        return TMeUrlTypeChatInvite(info)
