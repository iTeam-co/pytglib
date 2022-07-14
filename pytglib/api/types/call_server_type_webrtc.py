

from ..utils import Object


class CallServerTypeWebrtc(Object):
    """
    A WebRTC server 

    Attributes:
        ID (:obj:`str`): ``CallServerTypeWebrtc``

    Args:
        username (:obj:`str`):
            Username to be used for authentication 
        password (:obj:`str`):
            Authentication password 
        supports_turn (:obj:`bool`):
            True, if the server supports TURN 
        supports_stun (:obj:`bool`):
            True, if the server supports STUN

    Returns:
        CallServerType

    Raises:
        :class:`telegram.Error`
    """
    ID = "callServerTypeWebrtc"

    def __init__(self, username, password, supports_turn, supports_stun, **kwargs):
        
        self.username = username  # str
        self.password = password  # str
        self.supports_turn = supports_turn  # bool
        self.supports_stun = supports_stun  # bool

    @staticmethod
    def read(q: dict, *args) -> "CallServerTypeWebrtc":
        username = q.get('username')
        password = q.get('password')
        supports_turn = q.get('supports_turn')
        supports_stun = q.get('supports_stun')
        return CallServerTypeWebrtc(username, password, supports_turn, supports_stun)
