

from ..utils import Object


class GetTrendingStickerSets(Object):
    """
    Returns a list of trending sticker sets. For optimal performance, the number of returned sticker sets is chosen by TDLib

    Attributes:
        ID (:obj:`str`): ``GetTrendingStickerSets``

    Args:
        offset (:obj:`int`):
            The offset from which to return the sticker sets; must be non-negative
        limit (:obj:`int`):
            The maximum number of sticker sets to be returned; up to 100For optimal performance, the number of returned sticker sets is chosen by TDLib and can be smaller than the specified limit, even if the end of the list has not been reached

    Returns:
        TrendingStickerSets

    Raises:
        :class:`telegram.Error`
    """
    ID = "getTrendingStickerSets"

    def __init__(self, offset, limit, extra=None, **kwargs):
        self.extra = extra
        self.offset = offset  # int
        self.limit = limit  # int

    @staticmethod
    def read(q: dict, *args) -> "GetTrendingStickerSets":
        offset = q.get('offset')
        limit = q.get('limit')
        return GetTrendingStickerSets(offset, limit)
