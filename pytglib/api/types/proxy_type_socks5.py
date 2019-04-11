

from ..utils import Object


class ProxyTypeSocks5(Object):
    """
    A SOCKS5 proxy server 

    Attributes:
        ID (:obj:`str`): ``ProxyTypeSocks5``

    Args:
        username (:obj:`str`):
            Username for logging in; may be empty 
        password (:obj:`str`):
            Password for logging in; may be empty

    Returns:
        ProxyType

    Raises:
        :class:`telegram.Error`
    """
    ID = "proxyTypeSocks5"

    def __init__(self, username, password, **kwargs):
        
        self.username = username  # str
        self.password = password  # str

    @staticmethod
    def read(q: dict, *args) -> "ProxyTypeSocks5":
        username = q.get('username')
        password = q.get('password')
        return ProxyTypeSocks5(username, password)
