

from ..utils import Object


class GetTrendingStickerSets(Object):
    """
    Returns a list of trending sticker sets

    Attributes:
        ID (:obj:`str`): ``GetTrendingStickerSets``

    No parameters required.

    Returns:
        StickerSets

    Raises:
        :class:`telegram.Error`
    """
    ID = "getTrendingStickerSets"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "GetTrendingStickerSets":
        
        return GetTrendingStickerSets()
