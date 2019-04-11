

from ..utils import Object


class UpdateScopeNotificationSettings(Object):
    """
    Notification settings for some type of chats were updated 

    Attributes:
        ID (:obj:`str`): ``UpdateScopeNotificationSettings``

    Args:
        scope (:class:`telegram.api.types.NotificationSettingsScope`):
            Types of chats for which notification settings were updated 
        notification_settings (:class:`telegram.api.types.scopeNotificationSettings`):
            The new notification settings

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateScopeNotificationSettings"

    def __init__(self, scope, notification_settings, **kwargs):
        
        self.scope = scope  # NotificationSettingsScope
        self.notification_settings = notification_settings  # ScopeNotificationSettings

    @staticmethod
    def read(q: dict, *args) -> "UpdateScopeNotificationSettings":
        scope = Object.read(q.get('scope'))
        notification_settings = Object.read(q.get('notification_settings'))
        return UpdateScopeNotificationSettings(scope, notification_settings)
