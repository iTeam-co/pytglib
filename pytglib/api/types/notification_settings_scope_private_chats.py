

from ..utils import Object


class NotificationSettingsScopePrivateChats(Object):
    """
    Notification settings applied to all private and secret chats when the corresponding chat setting has a default value

    Attributes:
        ID (:obj:`str`): ``NotificationSettingsScopePrivateChats``

    No parameters required.

    Returns:
        NotificationSettingsScope

    Raises:
        :class:`telegram.Error`
    """
    ID = "notificationSettingsScopePrivateChats"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "NotificationSettingsScopePrivateChats":
        
        return NotificationSettingsScopePrivateChats()
