

from ..utils import Object


class AttachmentMenuBot(Object):
    """
    Represents a bot added to attachment menu

    Attributes:
        ID (:obj:`str`): ``AttachmentMenuBot``

    Args:
        bot_user_id (:obj:`int`):
            User identifier of the bot added to attachment menu
        supports_self_chat (:obj:`bool`):
            True, if the bot supports opening from attachment menu in the chat with the bot
        supports_user_chats (:obj:`bool`):
            True, if the bot supports opening from attachment menu in private chats with ordinary users
        supports_bot_chats (:obj:`bool`):
            True, if the bot supports opening from attachment menu in private chats with other bots
        supports_group_chats (:obj:`bool`):
            True, if the bot supports opening from attachment menu in basic group and supergroup chats
        supports_channel_chats (:obj:`bool`):
            True, if the bot supports opening from attachment menu in channel chats
        supports_settings (:obj:`bool`):
            True, if the bot supports "settings_button_pressed" event
        name (:obj:`str`):
            Name for the bot in attachment menu
        name_color (:class:`telegram.api.types.attachmentMenuBotColor`):
            Color to highlight selected name of the bot if appropriate; may be null
        default_icon (:class:`telegram.api.types.file`):
            Default attachment menu icon for the bot in SVG format; may be null
        ios_static_icon (:class:`telegram.api.types.file`):
            Attachment menu icon for the bot in SVG format for the official iOS app; may be null
        ios_animated_icon (:class:`telegram.api.types.file`):
            Attachment menu icon for the bot in TGS format for the official iOS app; may be null
        android_icon (:class:`telegram.api.types.file`):
            Attachment menu icon for the bot in TGS format for the official Android app; may be null
        macos_icon (:class:`telegram.api.types.file`):
            Attachment menu icon for the bot in TGS format for the official native macOS app; may be null
        icon_color (:class:`telegram.api.types.attachmentMenuBotColor`):
            Color to highlight selected icon of the bot if appropriate; may be null
        web_app_placeholder (:class:`telegram.api.types.file`):
            Default placeholder for opened Web Apps in SVG format; may be null

    Returns:
        AttachmentMenuBot

    Raises:
        :class:`telegram.Error`
    """
    ID = "attachmentMenuBot"

    def __init__(self, bot_user_id, supports_self_chat, supports_user_chats, supports_bot_chats, supports_group_chats, supports_channel_chats, supports_settings, name, name_color, default_icon, ios_static_icon, ios_animated_icon, android_icon, macos_icon, icon_color, web_app_placeholder, **kwargs):
        
        self.bot_user_id = bot_user_id  # int
        self.supports_self_chat = supports_self_chat  # bool
        self.supports_user_chats = supports_user_chats  # bool
        self.supports_bot_chats = supports_bot_chats  # bool
        self.supports_group_chats = supports_group_chats  # bool
        self.supports_channel_chats = supports_channel_chats  # bool
        self.supports_settings = supports_settings  # bool
        self.name = name  # str
        self.name_color = name_color  # AttachmentMenuBotColor
        self.default_icon = default_icon  # File
        self.ios_static_icon = ios_static_icon  # File
        self.ios_animated_icon = ios_animated_icon  # File
        self.android_icon = android_icon  # File
        self.macos_icon = macos_icon  # File
        self.icon_color = icon_color  # AttachmentMenuBotColor
        self.web_app_placeholder = web_app_placeholder  # File

    @staticmethod
    def read(q: dict, *args) -> "AttachmentMenuBot":
        bot_user_id = q.get('bot_user_id')
        supports_self_chat = q.get('supports_self_chat')
        supports_user_chats = q.get('supports_user_chats')
        supports_bot_chats = q.get('supports_bot_chats')
        supports_group_chats = q.get('supports_group_chats')
        supports_channel_chats = q.get('supports_channel_chats')
        supports_settings = q.get('supports_settings')
        name = q.get('name')
        name_color = Object.read(q.get('name_color'))
        default_icon = Object.read(q.get('default_icon'))
        ios_static_icon = Object.read(q.get('ios_static_icon'))
        ios_animated_icon = Object.read(q.get('ios_animated_icon'))
        android_icon = Object.read(q.get('android_icon'))
        macos_icon = Object.read(q.get('macos_icon'))
        icon_color = Object.read(q.get('icon_color'))
        web_app_placeholder = Object.read(q.get('web_app_placeholder'))
        return AttachmentMenuBot(bot_user_id, supports_self_chat, supports_user_chats, supports_bot_chats, supports_group_chats, supports_channel_chats, supports_settings, name, name_color, default_icon, ios_static_icon, ios_animated_icon, android_icon, macos_icon, icon_color, web_app_placeholder)
