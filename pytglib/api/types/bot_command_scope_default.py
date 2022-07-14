

from ..utils import Object


class BotCommandScopeDefault(Object):
    """
    A scope covering all users

    Attributes:
        ID (:obj:`str`): ``BotCommandScopeDefault``

    No parameters required.

    Returns:
        BotCommandScope

    Raises:
        :class:`telegram.Error`
    """
    ID = "botCommandScopeDefault"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "BotCommandScopeDefault":
        
        return BotCommandScopeDefault()
