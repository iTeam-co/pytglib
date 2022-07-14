

from ..utils import Object


class InternalLinkTypeBotStart(Object):
    """
    The link is a link to a chat with a Telegram bot. Call searchPublicChat with the given bot username, check that the user is a bot, show START button in the chat with the bot,and then call sendBotStartMessage with the given start parameter after the button is pressed

    Attributes:
        ID (:obj:`str`): ``InternalLinkTypeBotStart``

    Args:
        bot_username (:obj:`str`):
            Username of the bot 
        start_parameter (:obj:`str`):
            The parameter to be passed to sendBotStartMessage
        autostart (:obj:`bool`):
            True, if sendBotStartMessage must be called automatically without showing the START button

    Returns:
        InternalLinkType

    Raises:
        :class:`telegram.Error`
    """
    ID = "internalLinkTypeBotStart"

    def __init__(self, bot_username, start_parameter, autostart, **kwargs):
        
        self.bot_username = bot_username  # str
        self.start_parameter = start_parameter  # str
        self.autostart = autostart  # bool

    @staticmethod
    def read(q: dict, *args) -> "InternalLinkTypeBotStart":
        bot_username = q.get('bot_username')
        start_parameter = q.get('start_parameter')
        autostart = q.get('autostart')
        return InternalLinkTypeBotStart(bot_username, start_parameter, autostart)
