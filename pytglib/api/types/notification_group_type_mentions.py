

from ..utils import Object


class NotificationGroupTypeMentions(Object):
    """
    A group containing notifications of type notificationTypeNewMessage and notificationTypeNewPushMessage with unread mentions of the current user, replies to their messages, or a pinned message

    Attributes:
        ID (:obj:`str`): ``NotificationGroupTypeMentions``

    No parameters required.

    Returns:
        NotificationGroupType

    Raises:
        :class:`telegram.Error`
    """
    ID = "notificationGroupTypeMentions"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "NotificationGroupTypeMentions":
        
        return NotificationGroupTypeMentions()
