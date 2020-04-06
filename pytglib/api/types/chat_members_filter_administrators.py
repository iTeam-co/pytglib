

from ..utils import Object


class ChatMembersFilterAdministrators(Object):
    """
    Returns the owner and administrators

    Attributes:
        ID (:obj:`str`): ``ChatMembersFilterAdministrators``

    No parameters required.

    Returns:
        ChatMembersFilter

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatMembersFilterAdministrators"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatMembersFilterAdministrators":
        
        return ChatMembersFilterAdministrators()
