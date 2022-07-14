

from ..utils import Object


class ChatActionBarReportSpam(Object):
    """
    The chat can be reported as spam using the method reportChat with the reason chatReportReasonSpam

    Attributes:
        ID (:obj:`str`): ``ChatActionBarReportSpam``

    Args:
        can_unarchive (:obj:`bool`):
            If true, the chat was automatically archived and can be moved back to the main chat list using addChatToList simultaneously with setting chat notification settings to default using setChatNotificationSettings

    Returns:
        ChatActionBar

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatActionBarReportSpam"

    def __init__(self, can_unarchive, **kwargs):
        
        self.can_unarchive = can_unarchive  # bool

    @staticmethod
    def read(q: dict, *args) -> "ChatActionBarReportSpam":
        can_unarchive = q.get('can_unarchive')
        return ChatActionBarReportSpam(can_unarchive)
