

from ..utils import Object


class ChatNotificationSettings(Object):
    """
    Contains information about notification settings for a chat

    Attributes:
        ID (:obj:`str`): ``ChatNotificationSettings``

    Args:
        use_default_mute_for (:obj:`bool`):
            If true, mute_for is ignored and the value for the relevant type of chat is used instead 
        mute_for (:obj:`int`):
            Time left before notifications will be unmuted, in seconds
        use_default_sound (:obj:`bool`):
            If true, sound is ignored and the value for the relevant type of chat is used instead 
        sound (:obj:`str`):
            The name of an audio file to be used for notification sounds; only applies to iOS applications
        use_default_show_preview (:obj:`bool`):
            If true, show_preview is ignored and the value for the relevant type of chat is used instead 
        show_preview (:obj:`bool`):
            True, if message content should be displayed in notifications
        use_default_disable_pinned_message_notifications (:obj:`bool`):
            If true, disable_pinned_message_notifications is ignored and the value for the relevant type of chat is used instead 
        disable_pinned_message_notifications (:obj:`bool`):
            If true, notifications for incoming pinned messages will be created as for an ordinary unread message
        use_default_disable_mention_notifications (:obj:`bool`):
            If true, disable_mention_notifications is ignored and the value for the relevant type of chat is used instead 
        disable_mention_notifications (:obj:`bool`):
            If true, notifications for messages with mentions will be created as for an ordinary unread message

    Returns:
        ChatNotificationSettings

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatNotificationSettings"

    def __init__(self, use_default_mute_for, mute_for, use_default_sound, sound, use_default_show_preview, show_preview, use_default_disable_pinned_message_notifications, disable_pinned_message_notifications, use_default_disable_mention_notifications, disable_mention_notifications, **kwargs):
        
        self.use_default_mute_for = use_default_mute_for  # bool
        self.mute_for = mute_for  # int
        self.use_default_sound = use_default_sound  # bool
        self.sound = sound  # str
        self.use_default_show_preview = use_default_show_preview  # bool
        self.show_preview = show_preview  # bool
        self.use_default_disable_pinned_message_notifications = use_default_disable_pinned_message_notifications  # bool
        self.disable_pinned_message_notifications = disable_pinned_message_notifications  # bool
        self.use_default_disable_mention_notifications = use_default_disable_mention_notifications  # bool
        self.disable_mention_notifications = disable_mention_notifications  # bool

    @staticmethod
    def read(q: dict, *args) -> "ChatNotificationSettings":
        use_default_mute_for = q.get('use_default_mute_for')
        mute_for = q.get('mute_for')
        use_default_sound = q.get('use_default_sound')
        sound = q.get('sound')
        use_default_show_preview = q.get('use_default_show_preview')
        show_preview = q.get('show_preview')
        use_default_disable_pinned_message_notifications = q.get('use_default_disable_pinned_message_notifications')
        disable_pinned_message_notifications = q.get('disable_pinned_message_notifications')
        use_default_disable_mention_notifications = q.get('use_default_disable_mention_notifications')
        disable_mention_notifications = q.get('disable_mention_notifications')
        return ChatNotificationSettings(use_default_mute_for, mute_for, use_default_sound, sound, use_default_show_preview, show_preview, use_default_disable_pinned_message_notifications, disable_pinned_message_notifications, use_default_disable_mention_notifications, disable_mention_notifications)
