

from ..utils import Object


class MaskPosition(Object):
    """
    Position on a photo where a mask should be placed 

    Attributes:
        ID (:obj:`str`): ``MaskPosition``

    Args:
        point (:class:`telegram.api.types.MaskPoint`):
            Part of the face, relative to which the mask should be placed
        x_shift (:obj:`float`):
            Shift by X-axis measured in widths of the mask scaled to the face size, from left to right(For example, -10 will place the mask just to the left of the default mask position)
        y_shift (:obj:`float`):
            Shift by Y-axis measured in heights of the mask scaled to the face size, from top to bottom(For example, 10 will place the mask just below the default mask position)
        scale (:obj:`float`):
            Mask scaling coefficient(For example, 20 means a doubled size)

    Returns:
        MaskPosition

    Raises:
        :class:`telegram.Error`
    """
    ID = "maskPosition"

    def __init__(self, point, x_shift, y_shift, scale, **kwargs):
        
        self.point = point  # MaskPoint
        self.x_shift = x_shift  # float
        self.y_shift = y_shift  # float
        self.scale = scale  # float

    @staticmethod
    def read(q: dict, *args) -> "MaskPosition":
        point = Object.read(q.get('point'))
        x_shift = q.get('x_shift')
        y_shift = q.get('y_shift')
        scale = q.get('scale')
        return MaskPosition(point, x_shift, y_shift, scale)
