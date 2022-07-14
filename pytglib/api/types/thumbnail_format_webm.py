

from ..utils import Object


class ThumbnailFormatWebm(Object):
    """
    The thumbnail is in WEBM format. It will be used only for WEBM sticker sets

    Attributes:
        ID (:obj:`str`): ``ThumbnailFormatWebm``

    No parameters required.

    Returns:
        ThumbnailFormat

    Raises:
        :class:`telegram.Error`
    """
    ID = "thumbnailFormatWebm"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ThumbnailFormatWebm":
        
        return ThumbnailFormatWebm()
