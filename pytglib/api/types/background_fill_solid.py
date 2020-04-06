

from ..utils import Object


class BackgroundFillSolid(Object):
    """
    Describes a solid fill of a background 

    Attributes:
        ID (:obj:`str`): ``BackgroundFillSolid``

    Args:
        color (:obj:`int`):
            A color of the background in the RGB24 format

    Returns:
        BackgroundFill

    Raises:
        :class:`telegram.Error`
    """
    ID = "backgroundFillSolid"

    def __init__(self, color, **kwargs):
        
        self.color = color  # int

    @staticmethod
    def read(q: dict, *args) -> "BackgroundFillSolid":
        color = q.get('color')
        return BackgroundFillSolid(color)
