

from ..utils import Object


class ProxyTypeHttp(Object):
    """
    A HTTP transparent proxy server 

    Attributes:
        ID (:obj:`str`): ``ProxyTypeHttp``

    Args:
        username (:obj:`str`):
            Username for logging in; may be empty 
        password (:obj:`str`):
            Password for logging in; may be empty 
        http_only (:obj:`bool`):
            Pass true if the proxy supports only HTTP requests and doesn't support transparent TCP connections via HTTP CONNECT method

    Returns:
        ProxyType

    Raises:
        :class:`telegram.Error`
    """
    ID = "proxyTypeHttp"

    def __init__(self, username, password, http_only, **kwargs):
        
        self.username = username  # str
        self.password = password  # str
        self.http_only = http_only  # bool

    @staticmethod
    def read(q: dict, *args) -> "ProxyTypeHttp":
        username = q.get('username')
        password = q.get('password')
        http_only = q.get('http_only')
        return ProxyTypeHttp(username, password, http_only)
