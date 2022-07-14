

from ..utils import Object


class GetCommands(Object):
    """
    Returns the list of commands supported by the bot for the given user scope and language; for bots only

    Attributes:
        ID (:obj:`str`): ``GetCommands``

    Args:
        scope (:class:`telegram.api.types.BotCommandScope`):
            The scope to which the commands are relevant; pass null to get commands in the default bot command scope
        language_code (:obj:`str`):
            A two-letter ISO 639-1 language code or an empty string

    Returns:
        BotCommands

    Raises:
        :class:`telegram.Error`
    """
    ID = "getCommands"

    def __init__(self, scope, language_code, extra=None, **kwargs):
        self.extra = extra
        self.scope = scope  # BotCommandScope
        self.language_code = language_code  # str

    @staticmethod
    def read(q: dict, *args) -> "GetCommands":
        scope = Object.read(q.get('scope'))
        language_code = q.get('language_code')
        return GetCommands(scope, language_code)
