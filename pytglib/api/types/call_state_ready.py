

from ..utils import Object


class CallStateReady(Object):
    """
    The call is ready to use 

    Attributes:
        ID (:obj:`str`): ``CallStateReady``

    Args:
        protocol (:class:`telegram.api.types.callProtocol`):
            Call protocols supported by the peer 
        servers (List of :class:`telegram.api.types.callServer`):
            List of available call servers 
        config (:obj:`str`):
            A JSON-encoded call config 
        encryption_key (:obj:`bytes`):
            Call encryption key 
        emojis (List of :obj:`str`):
            Encryption key emojis fingerprint 
        allow_p2p (:obj:`bool`):
            True, if peer-to-peer connection is allowed by users privacy settings

    Returns:
        CallState

    Raises:
        :class:`telegram.Error`
    """
    ID = "callStateReady"

    def __init__(self, protocol, servers, config, encryption_key, emojis, allow_p2p, **kwargs):
        
        self.protocol = protocol  # CallProtocol
        self.servers = servers  # list of callServer
        self.config = config  # str
        self.encryption_key = encryption_key  # bytes
        self.emojis = emojis  # list of str
        self.allow_p2p = allow_p2p  # bool

    @staticmethod
    def read(q: dict, *args) -> "CallStateReady":
        protocol = Object.read(q.get('protocol'))
        servers = [Object.read(i) for i in q.get('servers', [])]
        config = q.get('config')
        encryption_key = q.get('encryption_key')
        emojis = q.get('emojis')
        allow_p2p = q.get('allow_p2p')
        return CallStateReady(protocol, servers, config, encryption_key, emojis, allow_p2p)
