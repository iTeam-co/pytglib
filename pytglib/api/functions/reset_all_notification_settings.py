

from ..utils import Object


class ResetAllNotificationSettings(Object):
    """
    Resets all notification settings to their default values. By default, all chats are unmuted, the sound is set to "default" and message previews are shown

    Attributes:
        ID (:obj:`str`): ``ResetAllNotificationSettings``

    No parameters required.

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "resetAllNotificationSettings"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "ResetAllNotificationSettings":
        
        return ResetAllNotificationSettings()
