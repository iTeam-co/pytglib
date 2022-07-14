

from ..utils import Object


class ThumbnailFormat(Object):
    """
    Describes format of a thumbnail

    No parameters required.
    """
    ID = "thumbnailFormat"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ThumbnailFormatTgs or ThumbnailFormatJpeg or ThumbnailFormatGif or ThumbnailFormatWebp or ThumbnailFormatWebm or ThumbnailFormatMpeg4 or ThumbnailFormatPng":
        if q.get("@type"):
            return Object.read(q)
        return ThumbnailFormat()
