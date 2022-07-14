

from ..utils import Object


class MaskPointChin(Object):
    """
    The mask is placed relatively to the chin

    Attributes:
        ID (:obj:`str`): ``MaskPointChin``

    No parameters required.

    Returns:
        MaskPoint

    Raises:
        :class:`telegram.Error`
    """
    ID = "maskPointChin"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "MaskPointChin":
        
        return MaskPointChin()
