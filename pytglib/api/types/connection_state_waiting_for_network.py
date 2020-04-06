

from ..utils import Object


class ConnectionStateWaitingForNetwork(Object):
    """
    Currently waiting for the network to become available. Use setNetworkType to change the available network type

    Attributes:
        ID (:obj:`str`): ``ConnectionStateWaitingForNetwork``

    No parameters required.

    Returns:
        ConnectionState

    Raises:
        :class:`telegram.Error`
    """
    ID = "connectionStateWaitingForNetwork"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ConnectionStateWaitingForNetwork":
        
        return ConnectionStateWaitingForNetwork()
