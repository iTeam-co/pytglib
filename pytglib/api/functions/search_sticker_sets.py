

from ..utils import Object


class SearchStickerSets(Object):
    """
    Searches for ordinary sticker sets by looking for specified query in their title and name. Excludes installed sticker sets from the results 

    Attributes:
        ID (:obj:`str`): ``SearchStickerSets``

    Args:
        query (:obj:`str`):
            Query to search for

    Returns:
        StickerSets

    Raises:
        :class:`telegram.Error`
    """
    ID = "searchStickerSets"

    def __init__(self, query, extra=None, **kwargs):
        self.extra = extra
        self.query = query  # str

    @staticmethod
    def read(q: dict, *args) -> "SearchStickerSets":
        query = q.get('query')
        return SearchStickerSets(query)
