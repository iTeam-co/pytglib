

from ..utils import Object


class BotCommandScopeAllPrivateChats(Object):
    """
    A scope covering all private chats

    Attributes:
        ID (:obj:`str`): ``BotCommandScopeAllPrivateChats``

    No parameters required.

    Returns:
        BotCommandScope

    Raises:
        :class:`telegram.Error`
    """
    ID = "botCommandScopeAllPrivateChats"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "BotCommandScopeAllPrivateChats":
        
        return BotCommandScopeAllPrivateChats()
