

from ..utils import Object


class ChatMembersFilterRestricted(Object):
    """
    Returns users under certain restrictions in the chat; can be used only by administrators in a supergroup

    Attributes:
        ID (:obj:`str`): ``ChatMembersFilterRestricted``

    No parameters required.

    Returns:
        ChatMembersFilter

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatMembersFilterRestricted"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatMembersFilterRestricted":
        
        return ChatMembersFilterRestricted()
