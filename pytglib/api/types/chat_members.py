

from ..utils import Object


class ChatMembers(Object):
    """
    Contains a list of chat members 

    Attributes:
        ID (:obj:`str`): ``ChatMembers``

    Args:
        total_count (:obj:`int`):
            Approximate total count of chat members found 
        members (List of :class:`telegram.api.types.chatMember`):
            A list of chat members

    Returns:
        ChatMembers

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatMembers"

    def __init__(self, total_count, members, **kwargs):
        
        self.total_count = total_count  # int
        self.members = members  # list of chatMember

    @staticmethod
    def read(q: dict, *args) -> "ChatMembers":
        total_count = q.get('total_count')
        members = [Object.read(i) for i in q.get('members', [])]
        return ChatMembers(total_count, members)
