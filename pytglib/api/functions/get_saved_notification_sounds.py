

from ..utils import Object


class GetSavedNotificationSounds(Object):
    """
    Returns list of saved notification sounds. If a sound isn't in the list, then default sound needs to be used

    Attributes:
        ID (:obj:`str`): ``GetSavedNotificationSounds``

    No parameters required.

    Returns:
        NotificationSounds

    Raises:
        :class:`telegram.Error`
    """
    ID = "getSavedNotificationSounds"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "GetSavedNotificationSounds":
        
        return GetSavedNotificationSounds()
