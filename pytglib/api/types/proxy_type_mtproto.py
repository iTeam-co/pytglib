

from ..utils import Object


class ProxyTypeMtproto(Object):
    """
    An MTProto proxy server 

    Attributes:
        ID (:obj:`str`): ``ProxyTypeMtproto``

    Args:
        secret (:obj:`str`):
            The proxy's secret in hexadecimal encoding

    Returns:
        ProxyType

    Raises:
        :class:`telegram.Error`
    """
    ID = "proxyTypeMtproto"

    def __init__(self, secret, **kwargs):
        
        self.secret = secret  # str

    @staticmethod
    def read(q: dict, *args) -> "ProxyTypeMtproto":
        secret = q.get('secret')
        return ProxyTypeMtproto(secret)
