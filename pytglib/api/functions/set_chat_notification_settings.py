

from ..utils import Object


class SetChatNotificationSettings(Object):
    """
    Changes the notification settings of a chat 

    Attributes:
        ID (:obj:`str`): ``SetChatNotificationSettings``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        notification_settings (:class:`telegram.api.types.chatNotificationSettings`):
            New notification settings for the chat

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setChatNotificationSettings"

    def __init__(self, chat_id, notification_settings, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.notification_settings = notification_settings  # ChatNotificationSettings

    @staticmethod
    def read(q: dict, *args) -> "SetChatNotificationSettings":
        chat_id = q.get('chat_id')
        notification_settings = Object.read(q.get('notification_settings'))
        return SetChatNotificationSettings(chat_id, notification_settings)
