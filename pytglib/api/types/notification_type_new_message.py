

from ..utils import Object


class NotificationTypeNewMessage(Object):
    """
    New message was received 

    Attributes:
        ID (:obj:`str`): ``NotificationTypeNewMessage``

    Args:
        message (:class:`telegram.api.types.message`):
            The message

    Returns:
        NotificationType

    Raises:
        :class:`telegram.Error`
    """
    ID = "notificationTypeNewMessage"

    def __init__(self, message, **kwargs):
        
        self.message = message  # Message

    @staticmethod
    def read(q: dict, *args) -> "NotificationTypeNewMessage":
        message = Object.read(q.get('message'))
        return NotificationTypeNewMessage(message)
