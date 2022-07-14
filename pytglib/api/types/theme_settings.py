

from ..utils import Object


class ThemeSettings(Object):
    """
    Describes theme settings

    Attributes:
        ID (:obj:`str`): ``ThemeSettings``

    Args:
        accent_color (:obj:`int`):
            Theme accent color in ARGB format
        background (:class:`telegram.api.types.background`):
            The background to be used in chats; may be null
        outgoing_message_fill (:class:`telegram.api.types.BackgroundFill`):
            The fill to be used as a background for outgoing messages
        animate_outgoing_message_fill (:obj:`bool`):
            If true, the freeform gradient fill needs to be animated on every sent message
        outgoing_message_accent_color (:obj:`int`):
            Accent color of outgoing messages in ARGB format

    Returns:
        ThemeSettings

    Raises:
        :class:`telegram.Error`
    """
    ID = "themeSettings"

    def __init__(self, accent_color, background, outgoing_message_fill, animate_outgoing_message_fill, outgoing_message_accent_color, **kwargs):
        
        self.accent_color = accent_color  # int
        self.background = background  # Background
        self.outgoing_message_fill = outgoing_message_fill  # BackgroundFill
        self.animate_outgoing_message_fill = animate_outgoing_message_fill  # bool
        self.outgoing_message_accent_color = outgoing_message_accent_color  # int

    @staticmethod
    def read(q: dict, *args) -> "ThemeSettings":
        accent_color = q.get('accent_color')
        background = Object.read(q.get('background'))
        outgoing_message_fill = Object.read(q.get('outgoing_message_fill'))
        animate_outgoing_message_fill = q.get('animate_outgoing_message_fill')
        outgoing_message_accent_color = q.get('outgoing_message_accent_color')
        return ThemeSettings(accent_color, background, outgoing_message_fill, animate_outgoing_message_fill, outgoing_message_accent_color)
