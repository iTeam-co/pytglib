

from ..utils import Object


class NotificationSettingsScopeGroupChats(Object):
    """
    Notification settings applied to all basic groups and supergroups when the corresponding chat setting has a default value

    Attributes:
        ID (:obj:`str`): ``NotificationSettingsScopeGroupChats``

    No parameters required.

    Returns:
        NotificationSettingsScope

    Raises:
        :class:`telegram.Error`
    """
    ID = "notificationSettingsScopeGroupChats"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "NotificationSettingsScopeGroupChats":
        
        return NotificationSettingsScopeGroupChats()
