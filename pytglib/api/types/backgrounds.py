

from ..utils import Object


class Backgrounds(Object):
    """
    Contains a list of backgrounds 

    Attributes:
        ID (:obj:`str`): ``Backgrounds``

    Args:
        backgrounds (List of :class:`telegram.api.types.background`):
            A list of backgrounds

    Returns:
        Backgrounds

    Raises:
        :class:`telegram.Error`
    """
    ID = "backgrounds"

    def __init__(self, backgrounds, **kwargs):
        
        self.backgrounds = backgrounds  # list of background

    @staticmethod
    def read(q: dict, *args) -> "Backgrounds":
        backgrounds = [Object.read(i) for i in q.get('backgrounds', [])]
        return Backgrounds(backgrounds)
