

from ..utils import Object


class MaskPointMouth(Object):
    """
    A mask should be placed relatively to the mouth

    Attributes:
        ID (:obj:`str`): ``MaskPointMouth``

    No parameters required.

    Returns:
        MaskPoint

    Raises:
        :class:`telegram.Error`
    """
    ID = "maskPointMouth"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "MaskPointMouth":
        
        return MaskPointMouth()
