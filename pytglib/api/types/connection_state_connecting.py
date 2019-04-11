

from ..utils import Object


class ConnectionStateConnecting(Object):
    """
    Currently establishing a connection to the Telegram servers

    Attributes:
        ID (:obj:`str`): ``ConnectionStateConnecting``

    No parameters required.

    Returns:
        ConnectionState

    Raises:
        :class:`telegram.Error`
    """
    ID = "connectionStateConnecting"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ConnectionStateConnecting":
        
        return ConnectionStateConnecting()
