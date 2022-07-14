

from ..utils import Object


class StickerTypeVideo(Object):
    """
    The sticker is a video in WEBM format

    Attributes:
        ID (:obj:`str`): ``StickerTypeVideo``

    No parameters required.

    Returns:
        StickerType

    Raises:
        :class:`telegram.Error`
    """
    ID = "stickerTypeVideo"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "StickerTypeVideo":
        
        return StickerTypeVideo()
