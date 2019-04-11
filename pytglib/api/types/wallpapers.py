

from ..utils import Object


class Wallpapers(Object):
    """
    Contains a list of wallpapers 

    Attributes:
        ID (:obj:`str`): ``Wallpapers``

    Args:
        wallpapers (List of :class:`telegram.api.types.wallpaper`):
            A list of wallpapers

    Returns:
        Wallpapers

    Raises:
        :class:`telegram.Error`
    """
    ID = "wallpapers"

    def __init__(self, wallpapers, **kwargs):
        
        self.wallpapers = wallpapers  # list of wallpaper

    @staticmethod
    def read(q: dict, *args) -> "Wallpapers":
        wallpapers = [Object.read(i) for i in q.get('wallpapers', [])]
        return Wallpapers(wallpapers)
