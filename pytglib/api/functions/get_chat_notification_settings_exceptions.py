

from ..utils import Object


class GetChatNotificationSettingsExceptions(Object):
    """
    Returns list of chats with non-default notification settings 

    Attributes:
        ID (:obj:`str`): ``GetChatNotificationSettingsExceptions``

    Args:
        scope (:class:`telegram.api.types.NotificationSettingsScope`):
            If specified, only chats from the specified scope will be returned 
        compare_sound (:obj:`bool`):
            If true, also chats with non-default sound will be returned

    Returns:
        Chats

    Raises:
        :class:`telegram.Error`
    """
    ID = "getChatNotificationSettingsExceptions"

    def __init__(self, scope, compare_sound, extra=None, **kwargs):
        self.extra = extra
        self.scope = scope  # NotificationSettingsScope
        self.compare_sound = compare_sound  # bool

    @staticmethod
    def read(q: dict, *args) -> "GetChatNotificationSettingsExceptions":
        scope = Object.read(q.get('scope'))
        compare_sound = q.get('compare_sound')
        return GetChatNotificationSettingsExceptions(scope, compare_sound)
