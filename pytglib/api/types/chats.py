

from ..utils import Object


class Chats(Object):
    """
    Represents a list of chats 

    Attributes:
        ID (:obj:`str`): ``Chats``

    Args:
        chat_ids (List of :obj:`int`):
            List of chat identifiers

    Returns:
        Chats

    Raises:
        :class:`telegram.Error`
    """
    ID = "chats"

    def __init__(self, chat_ids, **kwargs):
        
        self.chat_ids = chat_ids  # list of int

    @staticmethod
    def read(q: dict, *args) -> "Chats":
        chat_ids = q.get('chat_ids')
        return Chats(chat_ids)
