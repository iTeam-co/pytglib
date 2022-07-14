

from ..utils import Object


class ThumbnailFormatJpeg(Object):
    """
    The thumbnail is in JPEG format

    Attributes:
        ID (:obj:`str`): ``ThumbnailFormatJpeg``

    No parameters required.

    Returns:
        ThumbnailFormat

    Raises:
        :class:`telegram.Error`
    """
    ID = "thumbnailFormatJpeg"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ThumbnailFormatJpeg":
        
        return ThumbnailFormatJpeg()
