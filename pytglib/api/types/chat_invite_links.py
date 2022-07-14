

from ..utils import Object


class ChatInviteLinks(Object):
    """
    Contains a list of chat invite links 

    Attributes:
        ID (:obj:`str`): ``ChatInviteLinks``

    Args:
        total_count (:obj:`int`):
            Approximate total number of chat invite links found 
        invite_links (List of :class:`telegram.api.types.chatInviteLink`):
            List of invite links

    Returns:
        ChatInviteLinks

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatInviteLinks"

    def __init__(self, total_count, invite_links, **kwargs):
        
        self.total_count = total_count  # int
        self.invite_links = invite_links  # list of chatInviteLink

    @staticmethod
    def read(q: dict, *args) -> "ChatInviteLinks":
        total_count = q.get('total_count')
        invite_links = [Object.read(i) for i in q.get('invite_links', [])]
        return ChatInviteLinks(total_count, invite_links)
