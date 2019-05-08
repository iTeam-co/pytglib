

from ..utils import Object


class NetworkType(Object):
    """
    Represents the type of a network

    No parameters required.
    """
    ID = "networkType"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "NetworkTypeMobileRoaming or NetworkTypeMobile or NetworkTypeNone or NetworkTypeWiFi or NetworkTypeOther":
        if q.get("@type"):
            return Object.read(q)
        return NetworkType()
