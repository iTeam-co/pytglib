

from ..utils import Object


class OpenWebApp(Object):
    """
    Informs TDLib that a Web App is being opened from attachment menu, a botMenuButton button, an internalLinkTypeAttachmentMenuBot link, or an inlineKeyboardButtonTypeWebApp button.For each bot, a confirmation alert about data sent to the bot must be shown once

    Attributes:
        ID (:obj:`str`): ``OpenWebApp``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat in which the Web App is opened
        bot_user_id (:obj:`int`):
            Identifier of the bot, providing the Web App
        url (:obj:`str`):
            The URL from an inlineKeyboardButtonTypeWebApp button, a botMenuButton button, or an internalLinkTypeAttachmentMenuBot link, or an empty string otherwise
        theme (:class:`telegram.api.types.themeParameters`):
            Preferred Web App theme; pass null to use the default theme
        reply_to_message_id (:obj:`int`):
            Identifier of the replied message for the message sent by the Web App; 0 if none

    Returns:
        WebAppInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "openWebApp"

    def __init__(self, chat_id, bot_user_id, url, theme, reply_to_message_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.bot_user_id = bot_user_id  # int
        self.url = url  # str
        self.theme = theme  # ThemeParameters
        self.reply_to_message_id = reply_to_message_id  # int

    @staticmethod
    def read(q: dict, *args) -> "OpenWebApp":
        chat_id = q.get('chat_id')
        bot_user_id = q.get('bot_user_id')
        url = q.get('url')
        theme = Object.read(q.get('theme'))
        reply_to_message_id = q.get('reply_to_message_id')
        return OpenWebApp(chat_id, bot_user_id, url, theme, reply_to_message_id)
