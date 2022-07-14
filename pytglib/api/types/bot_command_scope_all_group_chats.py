

from ..utils import Object


class BotCommandScopeAllGroupChats(Object):
    """
    A scope covering all group and supergroup chats

    Attributes:
        ID (:obj:`str`): ``BotCommandScopeAllGroupChats``

    No parameters required.

    Returns:
        BotCommandScope

    Raises:
        :class:`telegram.Error`
    """
    ID = "botCommandScopeAllGroupChats"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "BotCommandScopeAllGroupChats":
        
        return BotCommandScopeAllGroupChats()
