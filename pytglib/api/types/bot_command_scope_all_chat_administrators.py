

from ..utils import Object


class BotCommandScopeAllChatAdministrators(Object):
    """
    A scope covering all group and supergroup chat administrators

    Attributes:
        ID (:obj:`str`): ``BotCommandScopeAllChatAdministrators``

    No parameters required.

    Returns:
        BotCommandScope

    Raises:
        :class:`telegram.Error`
    """
    ID = "botCommandScopeAllChatAdministrators"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "BotCommandScopeAllChatAdministrators":
        
        return BotCommandScopeAllChatAdministrators()
