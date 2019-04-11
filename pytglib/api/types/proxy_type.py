

from ..utils import Object


class ProxyType(Object):
    """
    Describes the type of the proxy server

    No parameters required.
    """
    ID = "proxyType"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ProxyTypeMtproto or ProxyTypeSocks5 or ProxyTypeHttp":
        if q.get("@type"):
            return Object.read(q)
        return ProxyType()
