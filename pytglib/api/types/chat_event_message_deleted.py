

from ..utils import Object


class ChatEventMessageDeleted(Object):
    """
    A message was deleted 

    Attributes:
        ID (:obj:`str`): ``ChatEventMessageDeleted``

    Args:
        message (:class:`telegram.api.types.message`):
            Deleted message

    Returns:
        ChatEventAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatEventMessageDeleted"

    def __init__(self, message, **kwargs):
        
        self.message = message  # Message

    @staticmethod
    def read(q: dict, *args) -> "ChatEventMessageDeleted":
        message = Object.read(q.get('message'))
        return ChatEventMessageDeleted(message)
