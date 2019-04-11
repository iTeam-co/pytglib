

from ..utils import Object


class CallConnection(Object):
    """
    Describes the address of UDP reflectors 

    Attributes:
        ID (:obj:`str`): ``CallConnection``

    Args:
        id (:obj:`int`):
            Reflector identifier 
        ip (:obj:`str`):
            IPv4 reflector address 
        ipv6 (:obj:`str`):
            IPv6 reflector address 
        port (:obj:`int`):
            Reflector port number 
        peer_tag (:obj:`bytes`):
            Connection peer tag

    Returns:
        CallConnection

    Raises:
        :class:`telegram.Error`
    """
    ID = "callConnection"

    def __init__(self, id, ip, ipv6, port, peer_tag, **kwargs):
        
        self.id = id  # int
        self.ip = ip  # str
        self.ipv6 = ipv6  # str
        self.port = port  # int
        self.peer_tag = peer_tag  # bytes

    @staticmethod
    def read(q: dict, *args) -> "CallConnection":
        id = q.get('id')
        ip = q.get('ip')
        ipv6 = q.get('ipv6')
        port = q.get('port')
        peer_tag = q.get('peer_tag')
        return CallConnection(id, ip, ipv6, port, peer_tag)
