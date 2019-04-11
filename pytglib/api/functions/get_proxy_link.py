

from ..utils import Object


class GetProxyLink(Object):
    """
    Returns an HTTPS link, which can be used to add a proxy. Available only for SOCKS5 and MTProto proxies. Can be called before authorization 

    Attributes:
        ID (:obj:`str`): ``GetProxyLink``

    Args:
        proxy_id (:obj:`int`):
            Proxy identifier

    Returns:
        Text

    Raises:
        :class:`telegram.Error`
    """
    ID = "getProxyLink"

    def __init__(self, proxy_id, extra=None, **kwargs):
        self.extra = extra
        self.proxy_id = proxy_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetProxyLink":
        proxy_id = q.get('proxy_id')
        return GetProxyLink(proxy_id)
