

from ..utils import Object


class UpdateChatNotificationSettings(Object):
    """
    Notification settings for a chat were changed 

    Attributes:
        ID (:obj:`str`): ``UpdateChatNotificationSettings``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        notification_settings (:class:`telegram.api.types.chatNotificationSettings`):
            The new notification settings

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateChatNotificationSettings"

    def __init__(self, chat_id, notification_settings, **kwargs):
        
        self.chat_id = chat_id  # int
        self.notification_settings = notification_settings  # ChatNotificationSettings

    @staticmethod
    def read(q: dict, *args) -> "UpdateChatNotificationSettings":
        chat_id = q.get('chat_id')
        notification_settings = Object.read(q.get('notification_settings'))
        return UpdateChatNotificationSettings(chat_id, notification_settings)
