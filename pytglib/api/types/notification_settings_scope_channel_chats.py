

from ..utils import Object


class NotificationSettingsScopeChannelChats(Object):
    """
    Notification settings applied to all channels when the corresponding chat setting has a default value

    Attributes:
        ID (:obj:`str`): ``NotificationSettingsScopeChannelChats``

    No parameters required.

    Returns:
        NotificationSettingsScope

    Raises:
        :class:`telegram.Error`
    """
    ID = "notificationSettingsScopeChannelChats"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "NotificationSettingsScopeChannelChats":
        
        return NotificationSettingsScopeChannelChats()
