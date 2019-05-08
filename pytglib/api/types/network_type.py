

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
    def read(q: dict, *args) -> "NetworkTypeOther or NetworkTypeWiFi or NetworkTypeMobileRoaming or NetworkTypeNone or NetworkTypeMobile":
        if q.get("@type"):
            return Object.read(q)
        return NetworkType()
