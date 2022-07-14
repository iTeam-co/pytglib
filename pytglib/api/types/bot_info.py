

from ..utils import Object


class BotInfo(Object):
    """
    Contains information about a bot

    Attributes:
        ID (:obj:`str`): ``BotInfo``

    Args:
        share_text (:obj:`str`):
            The text that is shown on the bot's profile page and is sent together with the link when users share the bot
        description (:obj:`str`):
            The text shown in the chat with the bot if the chat is empty
        photo (:class:`telegram.api.types.photo`):
            Photo shown in the chat with the bot if the chat is empty; may be null
        animation (:class:`telegram.api.types.animation`):
            Animation shown in the chat with the bot if the chat is empty; may be null
        menu_button (:class:`telegram.api.types.botMenuButton`):
            Information about a button to show instead of the bot commands menu button; may be null if ordinary bot commands menu must be shown
        commands (List of :class:`telegram.api.types.botCommand`):
            List of the bot commands
        default_group_administrator_rights (:class:`telegram.api.types.chatAdministratorRights`):
            Default administrator rights for adding the bot to basic group and supergroup chats; may be null
        default_channel_administrator_rights (:class:`telegram.api.types.chatAdministratorRights`):
            Default administrator rights for adding the bot to channels; may be null

    Returns:
        BotInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "botInfo"

    def __init__(self, share_text, description, photo, animation, menu_button, commands, default_group_administrator_rights, default_channel_administrator_rights, **kwargs):
        
        self.share_text = share_text  # str
        self.description = description  # str
        self.photo = photo  # Photo
        self.animation = animation  # Animation
        self.menu_button = menu_button  # BotMenuButton
        self.commands = commands  # list of botCommand
        self.default_group_administrator_rights = default_group_administrator_rights  # ChatAdministratorRights
        self.default_channel_administrator_rights = default_channel_administrator_rights  # ChatAdministratorRights

    @staticmethod
    def read(q: dict, *args) -> "BotInfo":
        share_text = q.get('share_text')
        description = q.get('description')
        photo = Object.read(q.get('photo'))
        animation = Object.read(q.get('animation'))
        menu_button = Object.read(q.get('menu_button'))
        commands = [Object.read(i) for i in q.get('commands', [])]
        default_group_administrator_rights = Object.read(q.get('default_group_administrator_rights'))
        default_channel_administrator_rights = Object.read(q.get('default_channel_administrator_rights'))
        return BotInfo(share_text, description, photo, animation, menu_button, commands, default_group_administrator_rights, default_channel_administrator_rights)
