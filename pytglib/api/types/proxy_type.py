

from ..utils import Object


class ProxyType(Object):
    """
    Describes the type of a proxy server

    No parameters required.
    """
    ID = "proxyType"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ProxyTypeMtproto or ProxyTypeHttp or ProxyTypeSocks5":
        if q.get("@type"):
            return Object.read(q)
        return ProxyType()
