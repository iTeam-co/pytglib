

from ..utils import Object


class FoundMessages(Object):
    """
    Contains a list of messages found by a search 

    Attributes:
        ID (:obj:`str`): ``FoundMessages``

    Args:
        total_count (:obj:`int`):
            Approximate total number of messages found; -1 if unknown 
        messages (List of :class:`telegram.api.types.message`):
            List of messages 
        next_offset (:obj:`str`):
            The offset for the next requestIf empty, there are no more results

    Returns:
        FoundMessages

    Raises:
        :class:`telegram.Error`
    """
    ID = "foundMessages"

    def __init__(self, total_count, messages, next_offset, **kwargs):
        
        self.total_count = total_count  # int
        self.messages = messages  # list of message
        self.next_offset = next_offset  # str

    @staticmethod
    def read(q: dict, *args) -> "FoundMessages":
        total_count = q.get('total_count')
        messages = [Object.read(i) for i in q.get('messages', [])]
        next_offset = q.get('next_offset')
        return FoundMessages(total_count, messages, next_offset)
