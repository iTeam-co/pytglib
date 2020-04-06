

from ..utils import Object


class GetTopChats(Object):
    """
    Returns a list of frequently used chats. Supported only if the chat info database is enabled 

    Attributes:
        ID (:obj:`str`): ``GetTopChats``

    Args:
        category (:class:`telegram.api.types.TopChatCategory`):
            Category of chats to be returned 
        limit (:obj:`int`):
            The maximum number of chats to be returned; up to 30

    Returns:
        Chats

    Raises:
        :class:`telegram.Error`
    """
    ID = "getTopChats"

    def __init__(self, category, limit, extra=None, **kwargs):
        self.extra = extra
        self.category = category  # TopChatCategory
        self.limit = limit  # int

    @staticmethod
    def read(q: dict, *args) -> "GetTopChats":
        category = Object.read(q.get('category'))
        limit = q.get('limit')
        return GetTopChats(category, limit)
