

from ..utils import Object


class ChatActionBarReportAddBlock(Object):
    """
    The chat is a private or secret chat, which can be reported using the method reportChat, or the other user can be blocked using the method toggleMessageSenderIsBlocked, or the other user can be added to the contact list using the method addContact

    Attributes:
        ID (:obj:`str`): ``ChatActionBarReportAddBlock``

    Args:
        can_unarchive (:obj:`bool`):
            If true, the chat was automatically archived and can be moved back to the main chat list using addChatToList simultaneously with setting chat notification settings to default using setChatNotificationSettings
        distance (:obj:`int`):
            If non-negative, the current user was found by the peer through searchChatsNearby and this is the distance between the users

    Returns:
        ChatActionBar

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatActionBarReportAddBlock"

    def __init__(self, can_unarchive, distance, **kwargs):
        
        self.can_unarchive = can_unarchive  # bool
        self.distance = distance  # int

    @staticmethod
    def read(q: dict, *args) -> "ChatActionBarReportAddBlock":
        can_unarchive = q.get('can_unarchive')
        distance = q.get('distance')
        return ChatActionBarReportAddBlock(can_unarchive, distance)
