

from ..utils import Object


class NetworkTypeOther(Object):
    """
    A different network type (e.g., Ethernet network)

    Attributes:
        ID (:obj:`str`): ``NetworkTypeOther``

    No parameters required.

    Returns:
        NetworkType

    Raises:
        :class:`telegram.Error`
    """
    ID = "networkTypeOther"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "NetworkTypeOther":
        
        return NetworkTypeOther()
