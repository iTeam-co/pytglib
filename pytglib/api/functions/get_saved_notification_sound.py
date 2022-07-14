

from ..utils import Object


class GetSavedNotificationSound(Object):
    """
    Returns saved notification sound by its identifier. Returns a 404 error if there is no saved notification sound with the specified identifier 

    Attributes:
        ID (:obj:`str`): ``GetSavedNotificationSound``

    Args:
        notification_sound_id (:obj:`int`):
            Identifier of the notification sound

    Returns:
        NotificationSounds

    Raises:
        :class:`telegram.Error`
    """
    ID = "getSavedNotificationSound"

    def __init__(self, notification_sound_id, extra=None, **kwargs):
        self.extra = extra
        self.notification_sound_id = notification_sound_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetSavedNotificationSound":
        notification_sound_id = q.get('notification_sound_id')
        return GetSavedNotificationSound(notification_sound_id)
