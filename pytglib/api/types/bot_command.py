

from ..utils import Object


class BotCommand(Object):
    """
    Represents a command supported by a bot 

    Attributes:
        ID (:obj:`str`): ``BotCommand``

    Args:
        command (:obj:`str`):
            Text of the bot command 
        description (:obj:`str`):
            Description of the bot command

    Returns:
        BotCommand

    Raises:
        :class:`telegram.Error`
    """
    ID = "botCommand"

    def __init__(self, command, description, **kwargs):
        
        self.command = command  # str
        self.description = description  # str

    @staticmethod
    def read(q: dict, *args) -> "BotCommand":
        command = q.get('command')
        description = q.get('description')
        return BotCommand(command, description)
