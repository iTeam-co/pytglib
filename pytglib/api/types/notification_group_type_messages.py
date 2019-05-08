

from ..utils import Object


class NotificationGroupTypeMessages(Object):
    """
    A group containing notifications of type notificationTypeNewMessage and notificationTypeNewPushMessage with ordinary unread messages

    Attributes:
        ID (:obj:`str`): ``NotificationGroupTypeMessages``

    No parameters required.

    Returns:
        NotificationGroupType

    Raises:
        :class:`telegram.Error`
    """
    ID = "notificationGroupTypeMessages"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "NotificationGroupTypeMessages":
        
        return NotificationGroupTypeMessages()
