

from ..utils import Object


class RemoveSavedNotificationSound(Object):
    """
    Removes a notification sound from the list of saved notification sounds 

    Attributes:
        ID (:obj:`str`): ``RemoveSavedNotificationSound``

    Args:
        notification_sound_id (:obj:`int`):
            Identifier of the notification sound

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "removeSavedNotificationSound"

    def __init__(self, notification_sound_id, extra=None, **kwargs):
        self.extra = extra
        self.notification_sound_id = notification_sound_id  # int

    @staticmethod
    def read(q: dict, *args) -> "RemoveSavedNotificationSound":
        notification_sound_id = q.get('notification_sound_id')
        return RemoveSavedNotificationSound(notification_sound_id)
