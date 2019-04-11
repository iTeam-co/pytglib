

from ..utils import Object


class BotInfo(Object):
    """
    Provides information about a bot and its supported commands 

    Attributes:
        ID (:obj:`str`): ``BotInfo``

    Args:
        description (:obj:`str`):
            Long description shown on the user info page 
        commands (List of :class:`telegram.api.types.botCommand`):
            A list of commands supported by the bot

    Returns:
        BotInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "botInfo"

    def __init__(self, description, commands, **kwargs):
        
        self.description = description  # str
        self.commands = commands  # list of botCommand

    @staticmethod
    def read(q: dict, *args) -> "BotInfo":
        description = q.get('description')
        commands = [Object.read(i) for i in q.get('commands', [])]
        return BotInfo(description, commands)
