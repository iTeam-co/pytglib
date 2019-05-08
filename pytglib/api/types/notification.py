

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
        type (:class:`telegram.api.types.NotificationType`):
            Notification type

    Returns:
        Notification

    Raises:
        :class:`telegram.Error`
    """
    ID = "notification"

    def __init__(self, id, date, type, **kwargs):
        
        self.id = id  # int
        self.date = date  # int
        self.type = type  # NotificationType

    @staticmethod
    def read(q: dict, *args) -> "Notification":
        id = q.get('id')
        date = q.get('date')
        type = Object.read(q.get('type'))
        return Notification(id, date, type)
