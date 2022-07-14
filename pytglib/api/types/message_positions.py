

from ..utils import Object


class MessagePositions(Object):
    """
    Contains a list of message positions 

    Attributes:
        ID (:obj:`str`): ``MessagePositions``

    Args:
        total_count (:obj:`int`):
            Total number of messages found 
        positions (List of :class:`telegram.api.types.messagePosition`):
            List of message positions

    Returns:
        MessagePositions

    Raises:
        :class:`telegram.Error`
    """
    ID = "messagePositions"

    def __init__(self, total_count, positions, **kwargs):
        
        self.total_count = total_count  # int
        self.positions = positions  # list of messagePosition

    @staticmethod
    def read(q: dict, *args) -> "MessagePositions":
        total_count = q.get('total_count')
        positions = [Object.read(i) for i in q.get('positions', [])]
        return MessagePositions(total_count, positions)
