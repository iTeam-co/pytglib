

from ..utils import Object


class UpdateNewMessage(Object):
    """
    A new message was received; can also be an outgoing message 

    Attributes:
        ID (:obj:`str`): ``UpdateNewMessage``

    Args:
        message (:class:`telegram.api.types.message`):
            The new message

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateNewMessage"

    def __init__(self, message, **kwargs):
        
        self.message = message  # Message

    @staticmethod
    def read(q: dict, *args) -> "UpdateNewMessage":
        message = Object.read(q.get('message'))
        return UpdateNewMessage(message)
