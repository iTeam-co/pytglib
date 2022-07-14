

from ..utils import Object


class ChatTheme(Object):
    """
    Describes a chat theme

    Attributes:
        ID (:obj:`str`): ``ChatTheme``

    Args:
        name (:obj:`str`):
            Theme name
        light_settings (:class:`telegram.api.types.themeSettings`):
            Theme settings for a light chat theme
        dark_settings (:class:`telegram.api.types.themeSettings`):
            Theme settings for a dark chat theme

    Returns:
        ChatTheme

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatTheme"

    def __init__(self, name, light_settings, dark_settings, **kwargs):
        
        self.name = name  # str
        self.light_settings = light_settings  # ThemeSettings
        self.dark_settings = dark_settings  # ThemeSettings

    @staticmethod
    def read(q: dict, *args) -> "ChatTheme":
        name = q.get('name')
        light_settings = Object.read(q.get('light_settings'))
        dark_settings = Object.read(q.get('dark_settings'))
        return ChatTheme(name, light_settings, dark_settings)
