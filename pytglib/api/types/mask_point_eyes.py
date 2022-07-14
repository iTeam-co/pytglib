

from ..utils import Object


class MaskPointEyes(Object):
    """
    The mask is placed relatively to the eyes

    Attributes:
        ID (:obj:`str`): ``MaskPointEyes``

    No parameters required.

    Returns:
        MaskPoint

    Raises:
        :class:`telegram.Error`
    """
    ID = "maskPointEyes"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "MaskPointEyes":
        
        return MaskPointEyes()
