

from ..utils import Object


class RemoveNotificationGroup(Object):
    """
    Removes a group of active notifications. Needs to be called only if the notification group is removed by the current user 

    Attributes:
        ID (:obj:`str`): ``RemoveNotificationGroup``

    Args:
        notification_group_id (:obj:`int`):
            Notification group identifier 
        max_notification_id (:obj:`int`):
            The maximum identifier of removed notifications

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "removeNotificationGroup"

    def __init__(self, notification_group_id, max_notification_id, extra=None, **kwargs):
        self.extra = extra
        self.notification_group_id = notification_group_id  # int
        self.max_notification_id = max_notification_id  # int

    @staticmethod
    def read(q: dict, *args) -> "RemoveNotificationGroup":
        notification_group_id = q.get('notification_group_id')
        max_notification_id = q.get('max_notification_id')
        return RemoveNotificationGroup(notification_group_id, max_notification_id)
