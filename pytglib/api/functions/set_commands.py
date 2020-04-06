

from ..utils import Object


class SetCommands(Object):
    """
    Sets the list of commands supported by the bot; for bots only 

    Attributes:
        ID (:obj:`str`): ``SetCommands``

    Args:
        commands (List of :class:`telegram.api.types.botCommand`):
            List of the bot's commands

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setCommands"

    def __init__(self, commands, extra=None, **kwargs):
        self.extra = extra
        self.commands = commands  # list of botCommand

    @staticmethod
    def read(q: dict, *args) -> "SetCommands":
        commands = [Object.read(i) for i in q.get('commands', [])]
        return SetCommands(commands)
