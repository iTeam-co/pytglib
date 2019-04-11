

from ..utils import Object


class GetScopeNotificationSettings(Object):
    """
    Returns the notification settings for chats of a given type 

    Attributes:
        ID (:obj:`str`): ``GetScopeNotificationSettings``

    Args:
        scope (:class:`telegram.api.types.NotificationSettingsScope`):
            Types of chats for which to return the notification settings information

    Returns:
        ScopeNotificationSettings

    Raises:
        :class:`telegram.Error`
    """
    ID = "getScopeNotificationSettings"

    def __init__(self, scope, extra=None, **kwargs):
        self.extra = extra
        self.scope = scope  # NotificationSettingsScope

    @staticmethod
    def read(q: dict, *args) -> "GetScopeNotificationSettings":
        scope = Object.read(q.get('scope'))
        return GetScopeNotificationSettings(scope)
