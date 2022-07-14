

from ..utils import Object


class InternalLinkTypeChatInvite(Object):
    """
    The link is a chat invite link. Call checkChatInviteLink with the given invite link to process the link 

    Attributes:
        ID (:obj:`str`): ``InternalLinkTypeChatInvite``

    Args:
        invite_link (:obj:`str`):
            Internal representation of the invite link

    Returns:
        InternalLinkType

    Raises:
        :class:`telegram.Error`
    """
    ID = "internalLinkTypeChatInvite"

    def __init__(self, invite_link, **kwargs):
        
        self.invite_link = invite_link  # str

    @staticmethod
    def read(q: dict, *args) -> "InternalLinkTypeChatInvite":
        invite_link = q.get('invite_link')
        return InternalLinkTypeChatInvite(invite_link)
