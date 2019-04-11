

from ..utils import Object


class SetPinnedChats(Object):
    """
    Changes the order of pinned chats 

    Attributes:
        ID (:obj:`str`): ``SetPinnedChats``

    Args:
        chat_ids (List of :obj:`int`):
            The new list of pinned chats

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setPinnedChats"

    def __init__(self, chat_ids, extra=None, **kwargs):
        self.extra = extra
        self.chat_ids = chat_ids  # list of int

    @staticmethod
    def read(q: dict, *args) -> "SetPinnedChats":
        chat_ids = q.get('chat_ids')
        return SetPinnedChats(chat_ids)
