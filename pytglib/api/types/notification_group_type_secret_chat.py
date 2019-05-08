

from ..utils import Object


class NotificationGroupTypeSecretChat(Object):
    """
    A group containing a notification of type notificationTypeNewSecretChat

    Attributes:
        ID (:obj:`str`): ``NotificationGroupTypeSecretChat``

    No parameters required.

    Returns:
        NotificationGroupType

    Raises:
        :class:`telegram.Error`
    """
    ID = "notificationGroupTypeSecretChat"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "NotificationGroupTypeSecretChat":
        
        return NotificationGroupTypeSecretChat()
