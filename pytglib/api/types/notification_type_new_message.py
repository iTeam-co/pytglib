

from ..utils import Object


class NotificationTypeNewMessage(Object):
    """
    New message was received 

    Attributes:
        ID (:obj:`str`): ``NotificationTypeNewMessage``

    Args:
        message (:class:`telegram.api.types.message`):
            The message 
        show_preview (:obj:`bool`):
            True, if message content must be displayed in notifications

    Returns:
        NotificationType

    Raises:
        :class:`telegram.Error`
    """
    ID = "notificationTypeNewMessage"

    def __init__(self, message, show_preview, **kwargs):
        
        self.message = message  # Message
        self.show_preview = show_preview  # bool

    @staticmethod
    def read(q: dict, *args) -> "NotificationTypeNewMessage":
        message = Object.read(q.get('message'))
        show_preview = q.get('show_preview')
        return NotificationTypeNewMessage(message, show_preview)
