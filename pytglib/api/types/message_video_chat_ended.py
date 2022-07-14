

from ..utils import Object


class MessageVideoChatEnded(Object):
    """
    A message with information about an ended video chat 

    Attributes:
        ID (:obj:`str`): ``MessageVideoChatEnded``

    Args:
        duration (:obj:`int`):
            Call duration, in seconds

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageVideoChatEnded"

    def __init__(self, duration, **kwargs):
        
        self.duration = duration  # int

    @staticmethod
    def read(q: dict, *args) -> "MessageVideoChatEnded":
        duration = q.get('duration')
        return MessageVideoChatEnded(duration)
