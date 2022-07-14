

from ..utils import Object


class MessagePosition(Object):
    """
    Contains information about a message in a specific position 

    Attributes:
        ID (:obj:`str`): ``MessagePosition``

    Args:
        position (:obj:`int`):
            0-based message position in the full list of suitable messages 
        message_id (:obj:`int`):
            Message identifier 
        date (:obj:`int`):
            Point in time (Unix timestamp) when the message was sent

    Returns:
        MessagePosition

    Raises:
        :class:`telegram.Error`
    """
    ID = "messagePosition"

    def __init__(self, position, message_id, date, **kwargs):
        
        self.position = position  # int
        self.message_id = message_id  # int
        self.date = date  # int

    @staticmethod
    def read(q: dict, *args) -> "MessagePosition":
        position = q.get('position')
        message_id = q.get('message_id')
        date = q.get('date')
        return MessagePosition(position, message_id, date)
