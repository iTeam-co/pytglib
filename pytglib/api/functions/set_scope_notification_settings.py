

from ..utils import Object


class SetScopeNotificationSettings(Object):
    """
    Changes notification settings for chats of a given type 

    Attributes:
        ID (:obj:`str`): ``SetScopeNotificationSettings``

    Args:
        scope (:class:`telegram.api.types.NotificationSettingsScope`):
            Types of chats for which to change the notification settings 
        notification_settings (:class:`telegram.api.types.scopeNotificationSettings`):
            The new notification settings for the given scope

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setScopeNotificationSettings"

    def __init__(self, scope, notification_settings, extra=None, **kwargs):
        self.extra = extra
        self.scope = scope  # NotificationSettingsScope
        self.notification_settings = notification_settings  # ScopeNotificationSettings

    @staticmethod
    def read(q: dict, *args) -> "SetScopeNotificationSettings":
        scope = Object.read(q.get('scope'))
        notification_settings = Object.read(q.get('notification_settings'))
        return SetScopeNotificationSettings(scope, notification_settings)
