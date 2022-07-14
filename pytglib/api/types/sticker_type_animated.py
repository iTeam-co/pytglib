

from ..utils import Object


class StickerTypeAnimated(Object):
    """
    The sticker is an animation in TGS format

    Attributes:
        ID (:obj:`str`): ``StickerTypeAnimated``

    No parameters required.

    Returns:
        StickerType

    Raises:
        :class:`telegram.Error`
    """
    ID = "stickerTypeAnimated"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "StickerTypeAnimated":
        
        return StickerTypeAnimated()
