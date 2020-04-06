

from ..utils import Object


class SetChatNotificationSettings(Object):
    """
    Changes the notification settings of a chat. Notification settings of a chat with the current user (Saved Messages) can't be changed

    Attributes:
        ID (:obj:`str`): ``SetChatNotificationSettings``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        notification_settings (:class:`telegram.api.types.chatNotificationSettings`):
            New notification settings for the chatIf the chat is muted for more than 1 week, it is considered to be muted forever

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
