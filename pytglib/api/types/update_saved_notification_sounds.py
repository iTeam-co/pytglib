

from ..utils import Object


class UpdateSavedNotificationSounds(Object):
    """
    The list of saved notifications sounds was updated. This update may not be sent until information about a notification sound was requested for the first time 

    Attributes:
        ID (:obj:`str`): ``UpdateSavedNotificationSounds``

    Args:
        notification_sound_ids (List of :obj:`int`):
            The new list of identifiers of saved notification sounds

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateSavedNotificationSounds"

    def __init__(self, notification_sound_ids, **kwargs):
        
        self.notification_sound_ids = notification_sound_ids  # list of int

    @staticmethod
    def read(q: dict, *args) -> "UpdateSavedNotificationSounds":
        notification_sound_ids = q.get('notification_sound_ids')
        return UpdateSavedNotificationSounds(notification_sound_ids)
