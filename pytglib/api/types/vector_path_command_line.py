

from ..utils import Object


class VectorPathCommandLine(Object):
    """
    A straight line to a given point 

    Attributes:
        ID (:obj:`str`): ``VectorPathCommandLine``

    Args:
        end_point (:class:`telegram.api.types.point`):
            The end point of the straight line

    Returns:
        VectorPathCommand

    Raises:
        :class:`telegram.Error`
    """
    ID = "vectorPathCommandLine"

    def __init__(self, end_point, **kwargs):
        
        self.end_point = end_point  # Point

    @staticmethod
    def read(q: dict, *args) -> "VectorPathCommandLine":
        end_point = Object.read(q.get('end_point'))
        return VectorPathCommandLine(end_point)
