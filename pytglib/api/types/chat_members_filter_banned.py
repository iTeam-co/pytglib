

from ..utils import Object


class ChatMembersFilterBanned(Object):
    """
    Returns users banned from the chat; can be used only by administrators in a supergroup or in a channel

    Attributes:
        ID (:obj:`str`): ``ChatMembersFilterBanned``

    No parameters required.

    Returns:
        ChatMembersFilter

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatMembersFilterBanned"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatMembersFilterBanned":
        
        return ChatMembersFilterBanned()
