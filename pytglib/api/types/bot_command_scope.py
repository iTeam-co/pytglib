

from ..utils import Object


class BotCommandScope(Object):
    """
    Represents the scope to which bot commands are relevant

    No parameters required.
    """
    ID = "botCommandScope"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "BotCommandScopeChat or BotCommandScopeAllGroupChats or BotCommandScopeChatAdministrators or BotCommandScopeAllChatAdministrators or BotCommandScopeChatMember or BotCommandScopeDefault or BotCommandScopeAllPrivateChats":
        if q.get("@type"):
            return Object.read(q)
        return BotCommandScope()
