

from ..utils import Object


class ChatMembersFilterMembers(Object):
    """
    Returns all chat members, including restricted chat members

    Attributes:
        ID (:obj:`str`): ``ChatMembersFilterMembers``

    No parameters required.

    Returns:
        ChatMembersFilter

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatMembersFilterMembers"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatMembersFilterMembers":
        
        return ChatMembersFilterMembers()
