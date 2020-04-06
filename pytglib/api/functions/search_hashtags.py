

from ..utils import Object


class SearchHashtags(Object):
    """
    Searches for recently used hashtags by their prefix 

    Attributes:
        ID (:obj:`str`): ``SearchHashtags``

    Args:
        prefix (:obj:`str`):
            Hashtag prefix to search for 
        limit (:obj:`int`):
            The maximum number of hashtags to be returned

    Returns:
        Hashtags

    Raises:
        :class:`telegram.Error`
    """
    ID = "searchHashtags"

    def __init__(self, prefix, limit, extra=None, **kwargs):
        self.extra = extra
        self.prefix = prefix  # str
        self.limit = limit  # int

    @staticmethod
    def read(q: dict, *args) -> "SearchHashtags":
        prefix = q.get('prefix')
        limit = q.get('limit')
        return SearchHashtags(prefix, limit)
