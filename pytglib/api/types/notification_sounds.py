

from ..utils import Object


class NotificationSounds(Object):
    """
    Contains a list of notification sounds 

    Attributes:
        ID (:obj:`str`): ``NotificationSounds``

    Args:
        notification_sounds (List of :class:`telegram.api.types.notificationSound`):
            A list of notification sounds

    Returns:
        NotificationSounds

    Raises:
        :class:`telegram.Error`
    """
    ID = "notificationSounds"

    def __init__(self, notification_sounds, **kwargs):
        
        self.notification_sounds = notification_sounds  # list of notificationSound

    @staticmethod
    def read(q: dict, *args) -> "NotificationSounds":
        notification_sounds = [Object.read(i) for i in q.get('notification_sounds', [])]
        return NotificationSounds(notification_sounds)
