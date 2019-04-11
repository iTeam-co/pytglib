

from ..utils import Object


class EditProxy(Object):
    """
    Edits an existing proxy server for network requests. Can be called before authorization 

    Attributes:
        ID (:obj:`str`): ``EditProxy``

    Args:
        proxy_id (:obj:`int`):
            Proxy identifier 
        server (:obj:`str`):
            Proxy server IP address 
        port (:obj:`int`):
            Proxy server port 
        enable (:obj:`bool`):
            True, if the proxy should be enabled 
        type (:class:`telegram.api.types.ProxyType`):
            Proxy type

    Returns:
        Proxy

    Raises:
        :class:`telegram.Error`
    """
    ID = "editProxy"

    def __init__(self, proxy_id, server, port, enable, type, extra=None, **kwargs):
        self.extra = extra
        self.proxy_id = proxy_id  # int
        self.server = server  # str
        self.port = port  # int
        self.enable = enable  # bool
        self.type = type  # ProxyType

    @staticmethod
    def read(q: dict, *args) -> "EditProxy":
        proxy_id = q.get('proxy_id')
        server = q.get('server')
        port = q.get('port')
        enable = q.get('enable')
        type = Object.read(q.get('type'))
        return EditProxy(proxy_id, server, port, enable, type)
