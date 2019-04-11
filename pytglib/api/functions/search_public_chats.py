

from ..utils import Object


class SearchPublicChats(Object):
    """
    Searches public chats by looking for specified query in their username and title. Currently only private chats, supergroups and channels can be public. Returns a meaningful number of results. Returns nothing if the length of the searched username prefix is less than 5. Excludes private chats with contacts and chats from the chat list from the results 

    Attributes:
        ID (:obj:`str`): ``SearchPublicChats``

    Args:
        query (:obj:`str`):
            Query to search for

    Returns:
        Chats

    Raises:
        :class:`telegram.Error`
    """
    ID = "searchPublicChats"

    def __init__(self, query, extra=None, **kwargs):
        self.extra = extra
        self.query = query  # str

    @staticmethod
    def read(q: dict, *args) -> "SearchPublicChats":
        query = q.get('query')
        return SearchPublicChats(query)
