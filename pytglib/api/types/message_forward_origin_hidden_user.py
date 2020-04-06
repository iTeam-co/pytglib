

from ..utils import Object


class MessageForwardOriginHiddenUser(Object):
    """
    The message was originally written by a user, which is hidden by their privacy settings 

    Attributes:
        ID (:obj:`str`): ``MessageForwardOriginHiddenUser``

    Args:
        sender_name (:obj:`str`):
            Name of the sender

    Returns:
        MessageForwardOrigin

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageForwardOriginHiddenUser"

    def __init__(self, sender_name, **kwargs):
        
        self.sender_name = sender_name  # str

    @staticmethod
    def read(q: dict, *args) -> "MessageForwardOriginHiddenUser":
        sender_name = q.get('sender_name')
        return MessageForwardOriginHiddenUser(sender_name)
