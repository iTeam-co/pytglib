

from ..utils import Object


class ChatEventMemberLeft(Object):
    """
    A member left the chat

    Attributes:
        ID (:obj:`str`): ``ChatEventMemberLeft``

    No parameters required.

    Returns:
        ChatEventAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatEventMemberLeft"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatEventMemberLeft":
        
        return ChatEventMemberLeft()
