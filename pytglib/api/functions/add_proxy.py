

from ..utils import Object


class AddProxy(Object):
    """
    Adds a proxy server for network requests. Can be called before authorization 

    Attributes:
        ID (:obj:`str`): ``AddProxy``

    Args:
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
    ID = "addProxy"

    def __init__(self, server, port, enable, type, extra=None, **kwargs):
        self.extra = extra
        self.server = server  # str
        self.port = port  # int
        self.enable = enable  # bool
        self.type = type  # ProxyType

    @staticmethod
    def read(q: dict, *args) -> "AddProxy":
        server = q.get('server')
        port = q.get('port')
        enable = q.get('enable')
        type = Object.read(q.get('type'))
        return AddProxy(server, port, enable, type)
