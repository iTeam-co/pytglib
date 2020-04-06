

from ..utils import Object


class BackgroundTypeWallpaper(Object):
    """
    A wallpaper in JPEG format

    Attributes:
        ID (:obj:`str`): ``BackgroundTypeWallpaper``

    Args:
        is_blurred (:obj:`bool`):
            True, if the wallpaper must be downscaled to fit in 450x450 square and then box-blurred with radius 12
        is_moving (:obj:`bool`):
            True, if the background needs to be slightly moved when device is tilted

    Returns:
        BackgroundType

    Raises:
        :class:`telegram.Error`
    """
    ID = "backgroundTypeWallpaper"

    def __init__(self, is_blurred, is_moving, **kwargs):
        
        self.is_blurred = is_blurred  # bool
        self.is_moving = is_moving  # bool

    @staticmethod
    def read(q: dict, *args) -> "BackgroundTypeWallpaper":
        is_blurred = q.get('is_blurred')
        is_moving = q.get('is_moving')
        return BackgroundTypeWallpaper(is_blurred, is_moving)
