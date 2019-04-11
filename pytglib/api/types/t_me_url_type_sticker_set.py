

from ..utils import Object


class TMeUrlTypeStickerSet(Object):
    """
    A URL linking to a sticker set 

    Attributes:
        ID (:obj:`str`): ``TMeUrlTypeStickerSet``

    Args:
        sticker_set_id (:obj:`int`):
            Identifier of the sticker set

    Returns:
        TMeUrlType

    Raises:
        :class:`telegram.Error`
    """
    ID = "tMeUrlTypeStickerSet"

    def __init__(self, sticker_set_id, **kwargs):
        
        self.sticker_set_id = sticker_set_id  # int

    @staticmethod
    def read(q: dict, *args) -> "TMeUrlTypeStickerSet":
        sticker_set_id = q.get('sticker_set_id')
        return TMeUrlTypeStickerSet(sticker_set_id)
