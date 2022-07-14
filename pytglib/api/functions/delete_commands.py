

from ..utils import Object


class DeleteCommands(Object):
    """
    Deletes commands supported by the bot for the given user scope and language; for bots only

    Attributes:
        ID (:obj:`str`): ``DeleteCommands``

    Args:
        scope (:class:`telegram.api.types.BotCommandScope`):
            The scope to which the commands are relevant; pass null to delete commands in the default bot command scope
        language_code (:obj:`str`):
            A two-letter ISO 639-1 language code or an empty string

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "deleteCommands"

    def __init__(self, scope, language_code, extra=None, **kwargs):
        self.extra = extra
        self.scope = scope  # BotCommandScope
        self.language_code = language_code  # str

    @staticmethod
    def read(q: dict, *args) -> "DeleteCommands":
        scope = Object.read(q.get('scope'))
        language_code = q.get('language_code')
        return DeleteCommands(scope, language_code)
