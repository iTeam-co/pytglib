

from ..utils import Object


class Chats(Object):
    """
    Represents a list of chats 

    Attributes:
        ID (:obj:`str`): ``Chats``

    Args:
        total_count (:obj:`int`):
            Approximate total number of chats found 
        chat_ids (List of :obj:`int`):
            List of chat identifiers

    Returns:
        Chats

    Raises:
        :class:`telegram.Error`
    """
    ID = "chats"

    def __init__(self, total_count, chat_ids, **kwargs):
        
        self.total_count = total_count  # int
        self.chat_ids = chat_ids  # list of int

    @staticmethod
    def read(q: dict, *args) -> "Chats":
        total_count = q.get('total_count')
        chat_ids = q.get('chat_ids')
        return Chats(total_count, chat_ids)
