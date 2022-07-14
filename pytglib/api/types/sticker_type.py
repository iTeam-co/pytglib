

from ..utils import Object


class StickerType(Object):
    """
    Describes type of a sticker

    No parameters required.
    """
    ID = "stickerType"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "StickerTypeVideo or StickerTypeStatic or StickerTypeMask or StickerTypeAnimated":
        if q.get("@type"):
            return Object.read(q)
        return StickerType()
