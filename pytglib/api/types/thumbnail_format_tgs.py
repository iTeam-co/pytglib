

from ..utils import Object


class ThumbnailFormatTgs(Object):
    """
    The thumbnail is in TGS format. It will be used only for TGS sticker sets

    Attributes:
        ID (:obj:`str`): ``ThumbnailFormatTgs``

    No parameters required.

    Returns:
        ThumbnailFormat

    Raises:
        :class:`telegram.Error`
    """
    ID = "thumbnailFormatTgs"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ThumbnailFormatTgs":
        
        return ThumbnailFormatTgs()
