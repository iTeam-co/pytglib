

from ..utils import Object


class MessageForwardOriginMessageImport(Object):
    """
    The message was imported from an exported message history 

    Attributes:
        ID (:obj:`str`): ``MessageForwardOriginMessageImport``

    Args:
        sender_name (:obj:`str`):
            Name of the sender

    Returns:
        MessageForwardOrigin

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageForwardOriginMessageImport"

    def __init__(self, sender_name, **kwargs):
        
        self.sender_name = sender_name  # str

    @staticmethod
    def read(q: dict, *args) -> "MessageForwardOriginMessageImport":
        sender_name = q.get('sender_name')
        return MessageForwardOriginMessageImport(sender_name)
