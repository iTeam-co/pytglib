

from ..utils import Object


class CallServer(Object):
    """
    Describes a server for relaying call data 

    Attributes:
        ID (:obj:`str`): ``CallServer``

    Args:
        id (:obj:`int`):
            Server identifier 
        ip_address (:obj:`str`):
            Server IPv4 address 
        ipv6_address (:obj:`str`):
            Server IPv6 address 
        port (:obj:`int`):
            Server port number 
        type (:class:`telegram.api.types.CallServerType`):
            Server type

    Returns:
        CallServer

    Raises:
        :class:`telegram.Error`
    """
    ID = "callServer"

    def __init__(self, id, ip_address, ipv6_address, port, type, **kwargs):
        
        self.id = id  # int
        self.ip_address = ip_address  # str
        self.ipv6_address = ipv6_address  # str
        self.port = port  # int
        self.type = type  # CallServerType

    @staticmethod
    def read(q: dict, *args) -> "CallServer":
        id = q.get('id')
        ip_address = q.get('ip_address')
        ipv6_address = q.get('ipv6_address')
        port = q.get('port')
        type = Object.read(q.get('type'))
        return CallServer(id, ip_address, ipv6_address, port, type)
