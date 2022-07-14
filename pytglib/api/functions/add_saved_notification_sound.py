

from ..utils import Object


class AddSavedNotificationSound(Object):
    """
    Adds a new notification sound to the list of saved notification sounds. The new notification sound is added to the top of the list. If it is already in the list, its position isn't changed 

    Attributes:
        ID (:obj:`str`): ``AddSavedNotificationSound``

    Args:
        sound (:class:`telegram.api.types.InputFile`):
            Notification sound file to add

    Returns:
        NotificationSound

    Raises:
        :class:`telegram.Error`
    """
    ID = "addSavedNotificationSound"

    def __init__(self, sound, extra=None, **kwargs):
        self.extra = extra
        self.sound = sound  # InputFile

    @staticmethod
    def read(q: dict, *args) -> "AddSavedNotificationSound":
        sound = Object.read(q.get('sound'))
        return AddSavedNotificationSound(sound)
