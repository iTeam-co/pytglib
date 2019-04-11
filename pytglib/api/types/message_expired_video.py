

from ..utils import Object


class MessageExpiredVideo(Object):
    """
    An expired video message (self-destructed after TTL has elapsed)

    Attributes:
        ID (:obj:`str`): ``MessageExpiredVideo``

    No parameters required.

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageExpiredVideo"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "MessageExpiredVideo":
        
        return MessageExpiredVideo()
