

from ..utils import Object


class StickerTypeStatic(Object):
    """
    The sticker is an image in WEBP format

    Attributes:
        ID (:obj:`str`): ``StickerTypeStatic``

    No parameters required.

    Returns:
        StickerType

    Raises:
        :class:`telegram.Error`
    """
    ID = "stickerTypeStatic"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "StickerTypeStatic":
        
        return StickerTypeStatic()
