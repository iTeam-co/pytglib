

from ..utils import Object


class BackgroundFill(Object):
    """
    Describes a fill of a background

    No parameters required.
    """
    ID = "backgroundFill"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "BackgroundFillSolid or BackgroundFillFreeformGradient or BackgroundFillGradient":
        if q.get("@type"):
            return Object.read(q)
        return BackgroundFill()
