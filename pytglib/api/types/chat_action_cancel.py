

from ..utils import Object


class ChatActionCancel(Object):
    """
    The user has cancelled the previous action

    Attributes:
        ID (:obj:`str`): ``ChatActionCancel``

    No parameters required.

    Returns:
        ChatAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatActionCancel"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatActionCancel":
        
        return ChatActionCancel()
