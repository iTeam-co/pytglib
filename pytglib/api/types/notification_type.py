

from ..utils import Object


class NotificationType(Object):
    """
    Contains detailed information about a notification

    No parameters required.
    """
    ID = "notificationType"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "NotificationTypeNewCall or NotificationTypeNewMessage or NotificationTypeNewPushMessage or NotificationTypeNewSecretChat":
        if q.get("@type"):
            return Object.read(q)
        return NotificationType()
