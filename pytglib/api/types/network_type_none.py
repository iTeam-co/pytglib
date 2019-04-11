

from ..utils import Object


class NetworkTypeNone(Object):
    """
    The network is not available

    Attributes:
        ID (:obj:`str`): ``NetworkTypeNone``

    No parameters required.

    Returns:
        NetworkType

    Raises:
        :class:`telegram.Error`
    """
    ID = "networkTypeNone"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "NetworkTypeNone":
        
        return NetworkTypeNone()
