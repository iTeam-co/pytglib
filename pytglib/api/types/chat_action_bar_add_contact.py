

from ..utils import Object


class ChatActionBarAddContact(Object):
    """
    The chat is a private or secret chat and the other user can be added to the contact list using the method addContact

    Attributes:
        ID (:obj:`str`): ``ChatActionBarAddContact``

    No parameters required.

    Returns:
        ChatActionBar

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatActionBarAddContact"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatActionBarAddContact":
        
        return ChatActionBarAddContact()
