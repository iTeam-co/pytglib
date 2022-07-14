

from ..utils import Object


class VectorPathCommand(Object):
    """
    Represents a vector path command

    No parameters required.
    """
    ID = "vectorPathCommand"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "VectorPathCommandLine or VectorPathCommandCubicBezierCurve":
        if q.get("@type"):
            return Object.read(q)
        return VectorPathCommand()
