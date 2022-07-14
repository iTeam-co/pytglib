

from ..utils import Object


class InternalLinkTypeProxy(Object):
    """
    The link is a link to a proxy. Call addProxy with the given parameters to process the link and add the proxy

    Attributes:
        ID (:obj:`str`): ``InternalLinkTypeProxy``

    Args:
        server (:obj:`str`):
            Proxy server IP address 
        port (:obj:`int`):
            Proxy server port 
        type (:class:`telegram.api.types.ProxyType`):
            Type of the proxy

    Returns:
        InternalLinkType

    Raises:
        :class:`telegram.Error`
    """
    ID = "internalLinkTypeProxy"

    def __init__(self, server, port, type, **kwargs):
        
        self.server = server  # str
        self.port = port  # int
        self.type = type  # ProxyType

    @staticmethod
    def read(q: dict, *args) -> "InternalLinkTypeProxy":
        server = q.get('server')
        port = q.get('port')
        type = Object.read(q.get('type'))
        return InternalLinkTypeProxy(server, port, type)
