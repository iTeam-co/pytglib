

from ..utils import Object


class RemoveNotification(Object):
    """
    Removes an active notification from notification list. Needs to be called only if the notification is removed by the current user 

    Attributes:
        ID (:obj:`str`): ``RemoveNotification``

    Args:
        notification_group_id (:obj:`int`):
            Identifier of notification group to which the notification belongs 
        notification_id (:obj:`int`):
            Identifier of removed notification

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "removeNotification"

    def __init__(self, notification_group_id, notification_id, extra=None, **kwargs):
        self.extra = extra
        self.notification_group_id = notification_group_id  # int
        self.notification_id = notification_id  # int

    @staticmethod
    def read(q: dict, *args) -> "RemoveNotification":
        notification_group_id = q.get('notification_group_id')
        notification_id = q.get('notification_id')
        return RemoveNotification(notification_group_id, notification_id)
