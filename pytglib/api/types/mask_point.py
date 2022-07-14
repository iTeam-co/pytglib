

from ..utils import Object


class MaskPoint(Object):
    """
    Part of the face, relative to which a mask is placed

    No parameters required.
    """
    ID = "maskPoint"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "MaskPointMouth or MaskPointChin or MaskPointForehead or MaskPointEyes":
        if q.get("@type"):
            return Object.read(q)
        return MaskPoint()
