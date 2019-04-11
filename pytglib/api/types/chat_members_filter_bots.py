

from ..utils import Object


class ChatMembersFilterBots(Object):
    """
    Returns bot members of the chat

    Attributes:
        ID (:obj:`str`): ``ChatMembersFilterBots``

    No parameters required.

    Returns:
        ChatMembersFilter

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatMembersFilterBots"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatMembersFilterBots":
        
        return ChatMembersFilterBots()
