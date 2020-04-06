

from ..utils import Object


class SearchInstalledStickerSets(Object):
    """
    Searches for installed sticker sets by looking for specified query in their title and name 

    Attributes:
        ID (:obj:`str`): ``SearchInstalledStickerSets``

    Args:
        is_masks (:obj:`bool`):
            Pass true to return mask sticker sets; pass false to return ordinary sticker sets 
        query (:obj:`str`):
            Query to search for 
        limit (:obj:`int`):
            The maximum number of sticker sets to return

    Returns:
        StickerSets

    Raises:
        :class:`telegram.Error`
    """
    ID = "searchInstalledStickerSets"

    def __init__(self, is_masks, query, limit, extra=None, **kwargs):
        self.extra = extra
        self.is_masks = is_masks  # bool
        self.query = query  # str
        self.limit = limit  # int

    @staticmethod
    def read(q: dict, *args) -> "SearchInstalledStickerSets":
        is_masks = q.get('is_masks')
        query = q.get('query')
        limit = q.get('limit')
        return SearchInstalledStickerSets(is_masks, query, limit)
