

from ..utils import Object


class ChatActionChoosingContact(Object):
    """
    The user is picking a contact to send

    Attributes:
        ID (:obj:`str`): ``ChatActionChoosingContact``

    No parameters required.

    Returns:
        ChatAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatActionChoosingContact"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatActionChoosingContact":
        
        return ChatActionChoosingContact()
