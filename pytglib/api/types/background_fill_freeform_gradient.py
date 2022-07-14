

from ..utils import Object


class BackgroundFillFreeformGradient(Object):
    """
    Describes a freeform gradient fill of a background 

    Attributes:
        ID (:obj:`str`): ``BackgroundFillFreeformGradient``

    Args:
        colors (List of :obj:`int`):
            A list of 3 or 4 colors of the freeform gradients in the RGB24 format

    Returns:
        BackgroundFill

    Raises:
        :class:`telegram.Error`
    """
    ID = "backgroundFillFreeformGradient"

    def __init__(self, colors, **kwargs):
        
        self.colors = colors  # list of int

    @staticmethod
    def read(q: dict, *args) -> "BackgroundFillFreeformGradient":
        colors = q.get('colors')
        return BackgroundFillFreeformGradient(colors)
