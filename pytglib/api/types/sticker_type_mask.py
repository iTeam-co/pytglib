

from ..utils import Object


class StickerTypeMask(Object):
    """
    The sticker is a mask in WEBP format to be placed on photos or videos 

    Attributes:
        ID (:obj:`str`): ``StickerTypeMask``

    Args:
        mask_position (:class:`telegram.api.types.maskPosition`):
            Position where the mask is placed; may be null

    Returns:
        StickerType

    Raises:
        :class:`telegram.Error`
    """
    ID = "stickerTypeMask"

    def __init__(self, mask_position, **kwargs):
        
        self.mask_position = mask_position  # MaskPosition

    @staticmethod
    def read(q: dict, *args) -> "StickerTypeMask":
        mask_position = Object.read(q.get('mask_position'))
        return StickerTypeMask(mask_position)
