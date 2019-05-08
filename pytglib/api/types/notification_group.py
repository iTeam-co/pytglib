

from ..utils import Object


class NotificationGroup(Object):
    """
    Describes a group of notifications 

    Attributes:
        ID (:obj:`str`): ``NotificationGroup``

    Args:
        id (:obj:`int`):
            Unique persistent auto-incremented from 1 identifier of the notification group 
        type (:class:`telegram.api.types.NotificationGroupType`):
            Type of the group
        chat_id (:obj:`int`):
            Identifier of a chat to which all notifications in the group belong
        total_count (:obj:`int`):
            Total number of active notifications in the group 
        notifications (List of :class:`telegram.api.types.notification`):
            The list of active notifications

    Returns:
        NotificationGroup

    Raises:
        :class:`telegram.Error`
    """
    ID = "notificationGroup"

    def __init__(self, id, type, chat_id, total_count, notifications, **kwargs):
        
        self.id = id  # int
        self.type = type  # NotificationGroupType
        self.chat_id = chat_id  # int
        self.total_count = total_count  # int
        self.notifications = notifications  # list of notification

    @staticmethod
    def read(q: dict, *args) -> "NotificationGroup":
        id = q.get('id')
        type = Object.read(q.get('type'))
        chat_id = q.get('chat_id')
        total_count = q.get('total_count')
        notifications = [Object.read(i) for i in q.get('notifications', [])]
        return NotificationGroup(id, type, chat_id, total_count, notifications)
