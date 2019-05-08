

from ..utils import Object


class MessagePinMessage(Object):
    """
    A message has been pinned 

    Attributes:
        ID (:obj:`str`): ``MessagePinMessage``

    Args:
        message_id (:obj:`int`):
            Identifier of the pinned message, can be an identifier of a deleted message or 0

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messagePinMessage"

    def __init__(self, message_id, **kwargs):
        
        self.message_id = message_id  # int

    @staticmethod
    def read(q: dict, *args) -> "MessagePinMessage":
        message_id = q.get('message_id')
        return MessagePinMessage(message_id)
