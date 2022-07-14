

from ..utils import Object


class SetCommands(Object):
    """
    Sets the list of commands supported by the bot for the given user scope and language; for bots only

    Attributes:
        ID (:obj:`str`): ``SetCommands``

    Args:
        scope (:class:`telegram.api.types.BotCommandScope`):
            The scope to which the commands are relevant; pass null to change commands in the default bot command scope
        language_code (:obj:`str`):
            A two-letter ISO 639-1 language codeIf empty, the commands will be applied to all users from the given scope, for which language there are no dedicated commands
        commands (List of :class:`telegram.api.types.botCommand`):
            List of the bot's commands

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setCommands"

    def __init__(self, scope, language_code, commands, extra=None, **kwargs):
        self.extra = extra
        self.scope = scope  # BotCommandScope
        self.language_code = language_code  # str
        self.commands = commands  # list of botCommand

    @staticmethod
    def read(q: dict, *args) -> "SetCommands":
        scope = Object.read(q.get('scope'))
        language_code = q.get('language_code')
        commands = [Object.read(i) for i in q.get('commands', [])]
        return SetCommands(scope, language_code, commands)
