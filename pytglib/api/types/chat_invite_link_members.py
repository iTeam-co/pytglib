

from ..utils import Object


class ChatInviteLinkMembers(Object):
    """
    Contains a list of chat members joined a chat via an invite link 

    Attributes:
        ID (:obj:`str`): ``ChatInviteLinkMembers``

    Args:
        total_count (:obj:`int`):
            Approximate total number of chat members found 
        members (List of :class:`telegram.api.types.chatInviteLinkMember`):
            List of chat members, joined a chat via an invite link

    Returns:
        ChatInviteLinkMembers

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatInviteLinkMembers"

    def __init__(self, total_count, members, **kwargs):
        
        self.total_count = total_count  # int
        self.members = members  # list of chatInviteLinkMember

    @staticmethod
    def read(q: dict, *args) -> "ChatInviteLinkMembers":
        total_count = q.get('total_count')
        members = [Object.read(i) for i in q.get('members', [])]
        return ChatInviteLinkMembers(total_count, members)
