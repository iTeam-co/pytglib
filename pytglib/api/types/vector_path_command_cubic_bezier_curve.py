

from ..utils import Object


class VectorPathCommandCubicBezierCurve(Object):
    """
    A cubic Bézier curve to a given point 

    Attributes:
        ID (:obj:`str`): ``VectorPathCommandCubicBezierCurve``

    Args:
        start_control_point (:class:`telegram.api.types.point`):
            The start control point of the curve 
        end_control_point (:class:`telegram.api.types.point`):
            The end control point of the curve 
        end_point (:class:`telegram.api.types.point`):
            The end point of the curve

    Returns:
        VectorPathCommand

    Raises:
        :class:`telegram.Error`
    """
    ID = "vectorPathCommandCubicBezierCurve"

    def __init__(self, start_control_point, end_control_point, end_point, **kwargs):
        
        self.start_control_point = start_control_point  # Point
        self.end_control_point = end_control_point  # Point
        self.end_point = end_point  # Point

    @staticmethod
    def read(q: dict, *args) -> "VectorPathCommandCubicBezierCurve":
        start_control_point = Object.read(q.get('start_control_point'))
        end_control_point = Object.read(q.get('end_control_point'))
        end_point = Object.read(q.get('end_point'))
        return VectorPathCommandCubicBezierCurve(start_control_point, end_control_point, end_point)
