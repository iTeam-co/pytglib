

from ..utils import Object


class ChatActionTyping(Object):
    """
    The user is typing a message

    Attributes:
        ID (:obj:`str`): ``ChatActionTyping``

    No parameters required.

    Returns:
        ChatAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatActionTyping"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatActionTyping":
        
        return ChatActionTyping()
