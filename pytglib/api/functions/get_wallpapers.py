

from ..utils import Object


class GetWallpapers(Object):
    """
    Returns background wallpapers

    Attributes:
        ID (:obj:`str`): ``GetWallpapers``

    No parameters required.

    Returns:
        Wallpapers

    Raises:
        :class:`telegram.Error`
    """
    ID = "getWallpapers"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "GetWallpapers":
        
        return GetWallpapers()
