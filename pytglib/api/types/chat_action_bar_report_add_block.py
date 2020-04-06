

from ..utils import Object


class ChatActionBarReportAddBlock(Object):
    """
    The chat is a private or secret chat, which can be reported using the method reportChat, or the other user can be added to the contact list using the method addContact, or the other user can be blocked using the method blockUser

    Attributes:
        ID (:obj:`str`): ``ChatActionBarReportAddBlock``

    No parameters required.

    Returns:
        ChatActionBar

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatActionBarReportAddBlock"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatActionBarReportAddBlock":
        
        return ChatActionBarReportAddBlock()
