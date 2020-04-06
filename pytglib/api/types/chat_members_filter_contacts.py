

from ..utils import Object


class ChatMembersFilterContacts(Object):
    """
    Returns contacts of the user

    Attributes:
        ID (:obj:`str`): ``ChatMembersFilterContacts``

    No parameters required.

    Returns:
        ChatMembersFilter

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatMembersFilterContacts"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatMembersFilterContacts":
        
        return ChatMembersFilterContacts()
