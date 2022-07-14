

from ..utils import Object


class TrendingStickerSets(Object):
    """
    Represents a list of trending sticker sets 

    Attributes:
        ID (:obj:`str`): ``TrendingStickerSets``

    Args:
        total_count (:obj:`int`):
            Approximate total number of trending sticker sets 
        sets (List of :class:`telegram.api.types.stickerSetInfo`):
            List of trending sticker sets 
        is_premium (:obj:`bool`):
            True, if the list contains sticker sets with premium stickers

    Returns:
        TrendingStickerSets

    Raises:
        :class:`telegram.Error`
    """
    ID = "trendingStickerSets"

    def __init__(self, total_count, sets, is_premium, **kwargs):
        
        self.total_count = total_count  # int
        self.sets = sets  # list of stickerSetInfo
        self.is_premium = is_premium  # bool

    @staticmethod
    def read(q: dict, *args) -> "TrendingStickerSets":
        total_count = q.get('total_count')
        sets = [Object.read(i) for i in q.get('sets', [])]
        is_premium = q.get('is_premium')
        return TrendingStickerSets(total_count, sets, is_premium)
