

from ..utils import Object


class ThumbnailFormatWebp(Object):
    """
    The thumbnail is in WEBP format. It will be used only for some stickers

    Attributes:
        ID (:obj:`str`): ``ThumbnailFormatWebp``

    No parameters required.

    Returns:
        ThumbnailFormat

    Raises:
        :class:`telegram.Error`
    """
    ID = "thumbnailFormatWebp"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ThumbnailFormatWebp":
        
        return ThumbnailFormatWebp()
