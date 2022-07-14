

from ..utils import Object


class UpdateStickerSet(Object):
    """
    A sticker set has changed 

    Attributes:
        ID (:obj:`str`): ``UpdateStickerSet``

    Args:
        sticker_set (:class:`telegram.api.types.stickerSet`):
            The sticker set

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateStickerSet"

    def __init__(self, sticker_set, **kwargs):
        
        self.sticker_set = sticker_set  # StickerSet

    @staticmethod
    def read(q: dict, *args) -> "UpdateStickerSet":
        sticker_set = Object.read(q.get('sticker_set'))
        return UpdateStickerSet(sticker_set)
