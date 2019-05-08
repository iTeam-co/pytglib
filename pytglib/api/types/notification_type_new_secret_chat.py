

from ..utils import Object


class NotificationTypeNewSecretChat(Object):
    """
    New secret chat was created

    Attributes:
        ID (:obj:`str`): ``NotificationTypeNewSecretChat``

    No parameters required.

    Returns:
        NotificationType

    Raises:
        :class:`telegram.Error`
    """
    ID = "notificationTypeNewSecretChat"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "NotificationTypeNewSecretChat":
        
        return NotificationTypeNewSecretChat()
