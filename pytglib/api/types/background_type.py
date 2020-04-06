

from ..utils import Object


class BackgroundType(Object):
    """
    Describes the type of a background

    No parameters required.
    """
    ID = "backgroundType"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "BackgroundTypePattern or BackgroundTypeWallpaper or BackgroundTypeFill":
        if q.get("@type"):
            return Object.read(q)
        return BackgroundType()
