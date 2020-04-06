

from ..utils import Object


class BackgroundFillGradient(Object):
    """
    Describes a gradient fill of a background 

    Attributes:
        ID (:obj:`str`): ``BackgroundFillGradient``

    Args:
        top_color (:obj:`int`):
            A top color of the background in the RGB24 format 
        bottom_color (:obj:`int`):
            A bottom color of the background in the RGB24 format
        rotation_angle (:obj:`int`):
            Clockwise rotation angle of the gradient, in degrees; 0-359Should be always divisible by 45

    Returns:
        BackgroundFill

    Raises:
        :class:`telegram.Error`
    """
    ID = "backgroundFillGradient"

    def __init__(self, top_color, bottom_color, rotation_angle, **kwargs):
        
        self.top_color = top_color  # int
        self.bottom_color = bottom_color  # int
        self.rotation_angle = rotation_angle  # int

    @staticmethod
    def read(q: dict, *args) -> "BackgroundFillGradient":
        top_color = q.get('top_color')
        bottom_color = q.get('bottom_color')
        rotation_angle = q.get('rotation_angle')
        return BackgroundFillGradient(top_color, bottom_color, rotation_angle)
