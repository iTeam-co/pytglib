

from ..utils import Object


class ChatEventMemberJoined(Object):
    """
    A new member joined the chat

    Attributes:
        ID (:obj:`str`): ``ChatEventMemberJoined``

    No parameters required.

    Returns:
        ChatEventAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatEventMemberJoined"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatEventMemberJoined":
        
        return ChatEventMemberJoined()
