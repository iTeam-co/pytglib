

from ..utils import Object


class Animations(Object):
    """
    Represents a list of animations 

    Attributes:
        ID (:obj:`str`): ``Animations``

    Args:
        animations (List of :class:`telegram.api.types.animation`):
            List of animations

    Returns:
        Animations

    Raises:
        :class:`telegram.Error`
    """
    ID = "animations"

    def __init__(self, animations, **kwargs):
        
        self.animations = animations  # list of animation

    @staticmethod
    def read(q: dict, *args) -> "Animations":
        animations = [Object.read(i) for i in q.get('animations', [])]
        return Animations(animations)
