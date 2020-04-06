

from ..utils import Object


class SearchChatsOnServer(Object):
    """
    Searches for the specified query in the title and username of already known chats via request to the server. Returns chats in the order seen in the chat list 

    Attributes:
        ID (:obj:`str`): ``SearchChatsOnServer``

    Args:
        query (:obj:`str`):
            Query to search for 
        limit (:obj:`int`):
            The maximum number of chats to be returned

    Returns:
        Chats

    Raises:
        :class:`telegram.Error`
    """
    ID = "searchChatsOnServer"

    def __init__(self, query, limit, extra=None, **kwargs):
        self.extra = extra
        self.query = query  # str
        self.limit = limit  # int

    @staticmethod
    def read(q: dict, *args) -> "SearchChatsOnServer":
        query = q.get('query')
        limit = q.get('limit')
        return SearchChatsOnServer(query, limit)
