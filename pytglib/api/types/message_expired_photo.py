

from ..utils import Object


class MessageExpiredPhoto(Object):
    """
    An expired photo message (self-destructed after TTL has elapsed)

    Attributes:
        ID (:obj:`str`): ``MessageExpiredPhoto``

    No parameters required.

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageExpiredPhoto"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "MessageExpiredPhoto":
        
        return MessageExpiredPhoto()
