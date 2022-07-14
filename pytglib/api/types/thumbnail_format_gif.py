

from ..utils import Object


class ThumbnailFormatGif(Object):
    """
    The thumbnail is in static GIF format. It will be used only for some bot inline results

    Attributes:
        ID (:obj:`str`): ``ThumbnailFormatGif``

    No parameters required.

    Returns:
        ThumbnailFormat

    Raises:
        :class:`telegram.Error`
    """
    ID = "thumbnailFormatGif"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ThumbnailFormatGif":
        
        return ThumbnailFormatGif()
