

from ..utils import Object


class ThumbnailFormatMpeg4(Object):
    """
    The thumbnail is in MPEG4 format. It will be used only for some animations and videos

    Attributes:
        ID (:obj:`str`): ``ThumbnailFormatMpeg4``

    No parameters required.

    Returns:
        ThumbnailFormat

    Raises:
        :class:`telegram.Error`
    """
    ID = "thumbnailFormatMpeg4"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ThumbnailFormatMpeg4":
        
        return ThumbnailFormatMpeg4()
