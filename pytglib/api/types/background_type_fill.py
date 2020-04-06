

from ..utils import Object


class BackgroundTypeFill(Object):
    """
    A filled background 

    Attributes:
        ID (:obj:`str`): ``BackgroundTypeFill``

    Args:
        fill (:class:`telegram.api.types.BackgroundFill`):
            Description of the background fill

    Returns:
        BackgroundType

    Raises:
        :class:`telegram.Error`
    """
    ID = "backgroundTypeFill"

    def __init__(self, fill, **kwargs):
        
        self.fill = fill  # BackgroundFill

    @staticmethod
    def read(q: dict, *args) -> "BackgroundTypeFill":
        fill = Object.read(q.get('fill'))
        return BackgroundTypeFill(fill)
