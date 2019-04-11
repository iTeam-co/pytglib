

from ..utils import Object


class CallStateReady(Object):
    """
    The call is ready to use 

    Attributes:
        ID (:obj:`str`): ``CallStateReady``

    Args:
        protocol (:class:`telegram.api.types.callProtocol`):
            Call protocols supported by the peer 
        connections (List of :class:`telegram.api.types.callConnection`):
            Available UDP reflectors 
        config (:obj:`str`):
            A JSON-encoded call config 
        encryption_key (:obj:`bytes`):
            Call encryption key 
        emojis (List of :obj:`str`):
            Encryption key emojis fingerprint

    Returns:
        CallState

    Raises:
        :class:`telegram.Error`
    """
    ID = "callStateReady"

    def __init__(self, protocol, connections, config, encryption_key, emojis, **kwargs):
        
        self.protocol = protocol  # CallProtocol
        self.connections = connections  # list of callConnection
        self.config = config  # str
        self.encryption_key = encryption_key  # bytes
        self.emojis = emojis  # list of str

    @staticmethod
    def read(q: dict, *args) -> "CallStateReady":
        protocol = Object.read(q.get('protocol'))
        connections = [Object.read(i) for i in q.get('connections', [])]
        config = q.get('config')
        encryption_key = q.get('encryption_key')
        emojis = q.get('emojis')
        return CallStateReady(protocol, connections, config, encryption_key, emojis)
