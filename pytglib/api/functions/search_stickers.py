

from ..utils import Object


class SearchStickers(Object):
    """
    Searches for stickers from public sticker sets that correspond to a given emoji 

    Attributes:
        ID (:obj:`str`): ``SearchStickers``

    Args:
        emoji (:obj:`str`):
            String representation of emoji; must be non-empty 
        limit (:obj:`int`):
            The maximum number of stickers to be returned

    Returns:
        Stickers

    Raises:
        :class:`telegram.Error`
    """
    ID = "searchStickers"

    def __init__(self, emoji, limit, extra=None, **kwargs):
        self.extra = extra
        self.emoji = emoji  # str
        self.limit = limit  # int

    @staticmethod
    def read(q: dict, *args) -> "SearchStickers":
        emoji = q.get('emoji')
        limit = q.get('limit')
        return SearchStickers(emoji, limit)
