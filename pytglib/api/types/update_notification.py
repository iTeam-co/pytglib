

from ..utils import Object


class UpdateNotification(Object):
    """
    A notification was changed 

    Attributes:
        ID (:obj:`str`): ``UpdateNotification``

    Args:
        notification_group_id (:obj:`int`):
            Unique notification group identifier 
        notification (:class:`telegram.api.types.notification`):
            Changed notification

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateNotification"

    def __init__(self, notification_group_id, notification, **kwargs):
        
        self.notification_group_id = notification_group_id  # int
        self.notification = notification  # Notification

    @staticmethod
    def read(q: dict, *args) -> "UpdateNotification":
        notification_group_id = q.get('notification_group_id')
        notification = Object.read(q.get('notification'))
        return UpdateNotification(notification_group_id, notification)
