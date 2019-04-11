

from ..utils import Object


class NetworkTypeWiFi(Object):
    """
    A Wi-Fi network

    Attributes:
        ID (:obj:`str`): ``NetworkTypeWiFi``

    No parameters required.

    Returns:
        NetworkType

    Raises:
        :class:`telegram.Error`
    """
    ID = "networkTypeWiFi"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "NetworkTypeWiFi":
        
        return NetworkTypeWiFi()
