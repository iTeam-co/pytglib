

from ..utils import Object


class Point(Object):
    """
    A point on a Cartesian plane 

    Attributes:
        ID (:obj:`str`): ``Point``

    Args:
        x (:obj:`float`):
            The point's first coordinate 
        y (:obj:`float`):
            The point's second coordinate

    Returns:
        Point

    Raises:
        :class:`telegram.Error`
    """
    ID = "point"

    def __init__(self, x, y, **kwargs):
        
        self.x = x  # float
        self.y = y  # float

    @staticmethod
    def read(q: dict, *args) -> "Point":
        x = q.get('x')
        y = q.get('y')
        return Point(x, y)
