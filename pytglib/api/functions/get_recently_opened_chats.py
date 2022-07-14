

from ..utils import Object


class GetRecentlyOpenedChats(Object):
    """
    Returns recently opened chats, this is an offline request. Returns chats in the order of last opening 

    Attributes:
        ID (:obj:`str`): ``GetRecentlyOpenedChats``

    Args:
        limit (:obj:`int`):
            The maximum number of chats to be returned

    Returns:
        Chats

    Raises:
        :class:`telegram.Error`
    """
    ID = "getRecentlyOpenedChats"

    def __init__(self, limit, extra=None, **kwargs):
        self.extra = extra
        self.limit = limit  # int

    @staticmethod
    def read(q: dict, *args) -> "GetRecentlyOpenedChats":
        limit = q.get('limit')
        return GetRecentlyOpenedChats(limit)
