

from ..utils import Object


class StickerSets(Object):
    """
    Represents a list of sticker sets 

    Attributes:
        ID (:obj:`str`): ``StickerSets``

    Args:
        total_count (:obj:`int`):
            Approximate total number of sticker sets found 
        sets (List of :class:`telegram.api.types.stickerSetInfo`):
            List of sticker sets

    Returns:
        StickerSets

    Raises:
        :class:`telegram.Error`
    """
    ID = "stickerSets"

    def __init__(self, total_count, sets, **kwargs):
        
        self.total_count = total_count  # int
        self.sets = sets  # list of stickerSetInfo

    @staticmethod
    def read(q: dict, *args) -> "StickerSets":
        total_count = q.get('total_count')
        sets = [Object.read(i) for i in q.get('sets', [])]
        return StickerSets(total_count, sets)
