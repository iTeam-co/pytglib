

from ..utils import Object


class ConnectionStateConnectingToProxy(Object):
    """
    Currently establishing a connection with a proxy server

    Attributes:
        ID (:obj:`str`): ``ConnectionStateConnectingToProxy``

    No parameters required.

    Returns:
        ConnectionState

    Raises:
        :class:`telegram.Error`
    """
    ID = "connectionStateConnectingToProxy"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ConnectionStateConnectingToProxy":
        
        return ConnectionStateConnectingToProxy()
