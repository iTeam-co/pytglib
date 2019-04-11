

from ..utils import Object


class MaskPointForehead(Object):
    """
    A mask should be placed relatively to the forehead

    Attributes:
        ID (:obj:`str`): ``MaskPointForehead``

    No parameters required.

    Returns:
        MaskPoint

    Raises:
        :class:`telegram.Error`
    """
    ID = "maskPointForehead"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "MaskPointForehead":
        
        return MaskPointForehead()
