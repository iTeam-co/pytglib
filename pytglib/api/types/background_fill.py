

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
    def read(q: dict, *args) -> "BackgroundFillGradient or BackgroundFillSolid":
        if q.get("@type"):
            return Object.read(q)
        return BackgroundFill()
