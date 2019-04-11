

from ..utils import Object


class ChatEventMessagePinned(Object):
    """
    A message was pinned 

    Attributes:
        ID (:obj:`str`): ``ChatEventMessagePinned``

    Args:
        message (:class:`telegram.api.types.message`):
            Pinned message

    Returns:
        ChatEventAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatEventMessagePinned"

    def __init__(self, message, **kwargs):
        
        self.message = message  # Message

    @staticmethod
    def read(q: dict, *args) -> "ChatEventMessagePinned":
        message = Object.read(q.get('message'))
        return ChatEventMessagePinned(message)
