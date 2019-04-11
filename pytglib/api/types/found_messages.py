

from ..utils import Object


class FoundMessages(Object):
    """
    Contains a list of messages found by a search 

    Attributes:
        ID (:obj:`str`): ``FoundMessages``

    Args:
        messages (List of :class:`telegram.api.types.message`):
            List of messages 
        next_from_search_id (:obj:`int`):
            Value to pass as from_search_id to get more results

    Returns:
        FoundMessages

    Raises:
        :class:`telegram.Error`
    """
    ID = "foundMessages"

    def __init__(self, messages, next_from_search_id, **kwargs):
        
        self.messages = messages  # list of message
        self.next_from_search_id = next_from_search_id  # int

    @staticmethod
    def read(q: dict, *args) -> "FoundMessages":
        messages = [Object.read(i) for i in q.get('messages', [])]
        next_from_search_id = q.get('next_from_search_id')
        return FoundMessages(messages, next_from_search_id)
