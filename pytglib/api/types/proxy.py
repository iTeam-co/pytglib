

from ..utils import Object


class Proxy(Object):
    """
    Contains information about a proxy server 

    Attributes:
        ID (:obj:`str`): ``Proxy``

    Args:
        id (:obj:`int`):
            Unique identifier of the proxy 
        server (:obj:`str`):
            Proxy server IP address 
        port (:obj:`int`):
            Proxy server port 
        last_used_date (:obj:`int`):
            Point in time (Unix timestamp) when the proxy was last used; 0 if never 
        is_enabled (:obj:`bool`):
            True, if the proxy is enabled now 
        type (:class:`telegram.api.types.ProxyType`):
            Type of the proxy

    Returns:
        Proxy

    Raises:
        :class:`telegram.Error`
    """
    ID = "proxy"

    def __init__(self, id, server, port, last_used_date, is_enabled, type, **kwargs):
        
        self.id = id  # int
        self.server = server  # str
        self.port = port  # int
        self.last_used_date = last_used_date  # int
        self.is_enabled = is_enabled  # bool
        self.type = type  # ProxyType

    @staticmethod
    def read(q: dict, *args) -> "Proxy":
        id = q.get('id')
        server = q.get('server')
        port = q.get('port')
        last_used_date = q.get('last_used_date')
        is_enabled = q.get('is_enabled')
        type = Object.read(q.get('type'))
        return Proxy(id, server, port, last_used_date, is_enabled, type)
