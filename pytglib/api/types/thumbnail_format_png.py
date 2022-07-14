

from ..utils import Object


class ThumbnailFormatPng(Object):
    """
    The thumbnail is in PNG format. It will be used only for background patterns

    Attributes:
        ID (:obj:`str`): ``ThumbnailFormatPng``

    No parameters required.

    Returns:
        ThumbnailFormat

    Raises:
        :class:`telegram.Error`
    """
    ID = "thumbnailFormatPng"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ThumbnailFormatPng":
        
        return ThumbnailFormatPng()
