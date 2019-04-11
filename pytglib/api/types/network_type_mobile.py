

from ..utils import Object


class NetworkTypeMobile(Object):
    """
    A mobile network

    Attributes:
        ID (:obj:`str`): ``NetworkTypeMobile``

    No parameters required.

    Returns:
        NetworkType

    Raises:
        :class:`telegram.Error`
    """
    ID = "networkTypeMobile"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "NetworkTypeMobile":
        
        return NetworkTypeMobile()
