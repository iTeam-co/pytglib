

from ..utils import Object


class SearchContacts(Object):
    """
    Searches for the specified query in the first names, last names and usernames of the known user contacts 

    Attributes:
        ID (:obj:`str`): ``SearchContacts``

    Args:
        query (:obj:`str`):
            Query to search for; may be empty to return all contacts 
        limit (:obj:`int`):
            The maximum number of users to be returned

    Returns:
        Users

    Raises:
        :class:`telegram.Error`
    """
    ID = "searchContacts"

    def __init__(self, query, limit, extra=None, **kwargs):
        self.extra = extra
        self.query = query  # str
        self.limit = limit  # int

    @staticmethod
    def read(q: dict, *args) -> "SearchContacts":
        query = q.get('query')
        limit = q.get('limit')
        return SearchContacts(query, limit)
