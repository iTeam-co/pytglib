

from ..utils import Object


class NetworkTypeMobileRoaming(Object):
    """
    A mobile roaming network

    Attributes:
        ID (:obj:`str`): ``NetworkTypeMobileRoaming``

    No parameters required.

    Returns:
        NetworkType

    Raises:
        :class:`telegram.Error`
    """
    ID = "networkTypeMobileRoaming"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "NetworkTypeMobileRoaming":
        
        return NetworkTypeMobileRoaming()
