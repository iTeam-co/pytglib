

from ..utils import Object


class UpdateTrendingStickerSets(Object):
    """
    The list of trending sticker sets was updated or some of them were viewed 

    Attributes:
        ID (:obj:`str`): ``UpdateTrendingStickerSets``

    Args:
        sticker_sets (:class:`telegram.api.types.trendingStickerSets`):
            The prefix of the list of trending sticker sets with the newest trending sticker sets

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateTrendingStickerSets"

    def __init__(self, sticker_sets, **kwargs):
        
        self.sticker_sets = sticker_sets  # TrendingStickerSets

    @staticmethod
    def read(q: dict, *args) -> "UpdateTrendingStickerSets":
        sticker_sets = Object.read(q.get('sticker_sets'))
        return UpdateTrendingStickerSets(sticker_sets)
