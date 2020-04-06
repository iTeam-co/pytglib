

from ..utils import Object


class Notification(Object):
    """
    Contains information about a notification 

    Attributes:
        ID (:obj:`str`): ``Notification``

    Args:
        id (:obj:`int`):
            Unique persistent identifier of this notification 
        date (:obj:`int`):
            Notification date
        is_silent (:obj:`bool`):
            True, if the notification was initially silent 
        type (:class:`telegram.api.types.NotificationType`):
            Notification type

    Returns:
        Notification

    Raises:
        :class:`telegram.Error`
    """
    ID = "notification"

    def __init__(self, id, date, is_silent, type, **kwargs):
        
        self.id = id  # int
        self.date = date  # int
        self.is_silent = is_silent  # bool
        self.type = type  # NotificationType

    @staticmethod
    def read(q: dict, *args) -> "Notification":
        id = q.get('id')
        date = q.get('date')
        is_silent = q.get('is_silent')
        type = Object.read(q.get('type'))
        return Notification(id, date, is_silent, type)
