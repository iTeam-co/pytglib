

from ..utils import Object


class BotCommands(Object):
    """
    Contains a list of bot commands 

    Attributes:
        ID (:obj:`str`): ``BotCommands``

    Args:
        bot_user_id (:obj:`int`):
            Bot's user identifier 
        commands (List of :class:`telegram.api.types.botCommand`):
            List of bot commands

    Returns:
        BotCommands

    Raises:
        :class:`telegram.Error`
    """
    ID = "botCommands"

    def __init__(self, bot_user_id, commands, **kwargs):
        
        self.bot_user_id = bot_user_id  # int
        self.commands = commands  # list of botCommand

    @staticmethod
    def read(q: dict, *args) -> "BotCommands":
        bot_user_id = q.get('bot_user_id')
        commands = [Object.read(i) for i in q.get('commands', [])]
        return BotCommands(bot_user_id, commands)
