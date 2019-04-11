

from ..utils import Object


class MessageUnsupported(Object):
    """
    Message content that is not supported by the client

    Attributes:
        ID (:obj:`str`): ``MessageUnsupported``

    No parameters required.

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageUnsupported"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "MessageUnsupported":
        
        return MessageUnsupported()
