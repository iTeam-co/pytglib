

from ..utils import Object


class SearchChats(Object):
    """
    Searches for the specified query in the title and username of already known chats, this is an offline request. Returns chats in the order seen in the chat list 

    Attributes:
        ID (:obj:`str`): ``SearchChats``

    Args:
        query (:obj:`str`):
            Query to search forIf the query is empty, returns up to 20 recently found chats 
        limit (:obj:`int`):
            The maximum number of chats to be returned

    Returns:
        Chats

    Raises:
        :class:`telegram.Error`
    """
    ID = "searchChats"

    def __init__(self, query, limit, extra=None, **kwargs):
        self.extra = extra
        self.query = query  # str
        self.limit = limit  # int

    @staticmethod
    def read(q: dict, *args) -> "SearchChats":
        query = q.get('query')
        limit = q.get('limit')
        return SearchChats(query, limit)
