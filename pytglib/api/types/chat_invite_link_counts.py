

from ..utils import Object


class ChatInviteLinkCounts(Object):
    """
    Contains a list of chat invite link counts 

    Attributes:
        ID (:obj:`str`): ``ChatInviteLinkCounts``

    Args:
        invite_link_counts (List of :class:`telegram.api.types.chatInviteLinkCount`):
            List of invite link counts

    Returns:
        ChatInviteLinkCounts

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatInviteLinkCounts"

    def __init__(self, invite_link_counts, **kwargs):
        
        self.invite_link_counts = invite_link_counts  # list of chatInviteLinkCount

    @staticmethod
    def read(q: dict, *args) -> "ChatInviteLinkCounts":
        invite_link_counts = [Object.read(i) for i in q.get('invite_link_counts', [])]
        return ChatInviteLinkCounts(invite_link_counts)
