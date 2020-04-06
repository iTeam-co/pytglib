

from ..utils import Object


class TestProxy(Object):
    """
    Sends a simple network request to the Telegram servers via proxy; for testing only. Can be called before authorization 

    Attributes:
        ID (:obj:`str`): ``TestProxy``

    Args:
        server (:obj:`str`):
            Proxy server IP address 
        port (:obj:`int`):
            Proxy server port 
        type (:class:`telegram.api.types.ProxyType`):
            Proxy type
        dc_id (:obj:`int`):
            Identifier of a datacenter, with which to test connection 
        timeout (:obj:`float`):
            The maximum overall timeout for the request

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "testProxy"

    def __init__(self, server, port, type, dc_id, timeout, extra=None, **kwargs):
        self.extra = extra
        self.server = server  # str
        self.port = port  # int
        self.type = type  # ProxyType
        self.dc_id = dc_id  # int
        self.timeout = timeout  # float

    @staticmethod
    def read(q: dict, *args) -> "TestProxy":
        server = q.get('server')
        port = q.get('port')
        type = Object.read(q.get('type'))
        dc_id = q.get('dc_id')
        timeout = q.get('timeout')
        return TestProxy(server, port, type, dc_id, timeout)
