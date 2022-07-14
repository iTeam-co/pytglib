

from ..utils import Object


class CallServerTypeTelegramReflector(Object):
    """
    A Telegram call reflector 

    Attributes:
        ID (:obj:`str`): ``CallServerTypeTelegramReflector``

    Args:
        peer_tag (:obj:`bytes`):
            A peer tag to be used with the reflector 
        is_tcp (:obj:`bool`):
            True, if the server uses TCP instead of UDP

    Returns:
        CallServerType

    Raises:
        :class:`telegram.Error`
    """
    ID = "callServerTypeTelegramReflector"

    def __init__(self, peer_tag, is_tcp, **kwargs):
        
        self.peer_tag = peer_tag  # bytes
        self.is_tcp = is_tcp  # bool

    @staticmethod
    def read(q: dict, *args) -> "CallServerTypeTelegramReflector":
        peer_tag = q.get('peer_tag')
        is_tcp = q.get('is_tcp')
        return CallServerTypeTelegramReflector(peer_tag, is_tcp)
