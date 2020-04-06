

from ..utils import Object


class SendBotStartMessage(Object):
    """
    Invites a bot to a chat (if it is not yet a member) and sends it the /start command. Bots can't be invited to a private chat other than the chat with the bot. Bots can't be invited to channels (although they can be added as admins) and secret chats. Returns the sent message

    Attributes:
        ID (:obj:`str`): ``SendBotStartMessage``

    Args:
        bot_user_id (:obj:`int`):
            Identifier of the bot 
        chat_id (:obj:`int`):
            Identifier of the target chat 
        parameter (:obj:`str`):
            A hidden parameter sent to the bot for deep linking purposes (https://coretelegramorg/bots#deep-linking)

    Returns:
        Message

    Raises:
        :class:`telegram.Error`
    """
    ID = "sendBotStartMessage"

    def __init__(self, bot_user_id, chat_id, parameter, extra=None, **kwargs):
        self.extra = extra
        self.bot_user_id = bot_user_id  # int
        self.chat_id = chat_id  # int
        self.parameter = parameter  # str

    @staticmethod
    def read(q: dict, *args) -> "SendBotStartMessage":
        bot_user_id = q.get('bot_user_id')
        chat_id = q.get('chat_id')
        parameter = q.get('parameter')
        return SendBotStartMessage(bot_user_id, chat_id, parameter)
