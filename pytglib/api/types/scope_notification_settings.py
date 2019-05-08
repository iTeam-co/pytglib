

from ..utils import Object


class ScopeNotificationSettings(Object):
    """
    Contains information about notification settings for several chats

    Attributes:
        ID (:obj:`str`): ``ScopeNotificationSettings``

    Args:
        mute_for (:obj:`int`):
            Time left before notifications will be unmuted, in seconds
        sound (:obj:`str`):
            The name of an audio file to be used for notification sounds; only applies to iOS applications
        show_preview (:obj:`bool`):
            True, if message content should be displayed in notifications
        disable_pinned_message_notifications (:obj:`bool`):
            True, if notifications for incoming pinned messages will be created as for an ordinary unread message
        disable_mention_notifications (:obj:`bool`):
            True, if notifications for messages with mentions will be created as for an ordinary unread message

    Returns:
        ScopeNotificationSettings

    Raises:
        :class:`telegram.Error`
    """
    ID = "scopeNotificationSettings"

    def __init__(self, mute_for, sound, show_preview, disable_pinned_message_notifications, disable_mention_notifications, **kwargs):
        
        self.mute_for = mute_for  # int
        self.sound = sound  # str
        self.show_preview = show_preview  # bool
        self.disable_pinned_message_notifications = disable_pinned_message_notifications  # bool
        self.disable_mention_notifications = disable_mention_notifications  # bool

    @staticmethod
    def read(q: dict, *args) -> "ScopeNotificationSettings":
        mute_for = q.get('mute_for')
        sound = q.get('sound')
        show_preview = q.get('show_preview')
        disable_pinned_message_notifications = q.get('disable_pinned_message_notifications')
        disable_mention_notifications = q.get('disable_mention_notifications')
        return ScopeNotificationSettings(mute_for, sound, show_preview, disable_pinned_message_notifications, disable_mention_notifications)
