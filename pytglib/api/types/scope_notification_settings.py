

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

    Returns:
        ScopeNotificationSettings

    Raises:
        :class:`telegram.Error`
    """
    ID = "scopeNotificationSettings"

    def __init__(self, mute_for, sound, show_preview, **kwargs):
        
        self.mute_for = mute_for  # int
        self.sound = sound  # str
        self.show_preview = show_preview  # bool

    @staticmethod
    def read(q: dict, *args) -> "ScopeNotificationSettings":
        mute_for = q.get('mute_for')
        sound = q.get('sound')
        show_preview = q.get('show_preview')
        return ScopeNotificationSettings(mute_for, sound, show_preview)
