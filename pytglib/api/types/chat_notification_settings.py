

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

    Returns:
        ChatNotificationSettings

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatNotificationSettings"

    def __init__(self, use_default_mute_for, mute_for, use_default_sound, sound, use_default_show_preview, show_preview, **kwargs):
        
        self.use_default_mute_for = use_default_mute_for  # bool
        self.mute_for = mute_for  # int
        self.use_default_sound = use_default_sound  # bool
        self.sound = sound  # str
        self.use_default_show_preview = use_default_show_preview  # bool
        self.show_preview = show_preview  # bool

    @staticmethod
    def read(q: dict, *args) -> "ChatNotificationSettings":
        use_default_mute_for = q.get('use_default_mute_for')
        mute_for = q.get('mute_for')
        use_default_sound = q.get('use_default_sound')
        sound = q.get('sound')
        use_default_show_preview = q.get('use_default_show_preview')
        show_preview = q.get('show_preview')
        return ChatNotificationSettings(use_default_mute_for, mute_for, use_default_sound, sound, use_default_show_preview, show_preview)
