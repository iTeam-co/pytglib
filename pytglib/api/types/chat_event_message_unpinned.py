

from ..utils import Object


class ChatEventMessageUnpinned(Object):
    """
    A message was unpinned 

    Attributes:
        ID (:obj:`str`): ``ChatEventMessageUnpinned``

    Args:
        message (:class:`telegram.api.types.message`):
            Unpinned message

    Returns:
        ChatEventAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatEventMessageUnpinned"

    def __init__(self, message, **kwargs):
        
        self.message = message  # Message

    @staticmethod
    def read(q: dict, *args) -> "ChatEventMessageUnpinned":
        message = Object.read(q.get('message'))
        return ChatEventMessageUnpinned(message)
