

from ..utils import Object


class ConnectionState(Object):
    """
    Describes the current state of the connection to Telegram servers

    No parameters required.
    """
    ID = "connectionState"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ConnectionStateConnecting or ConnectionStateUpdating or ConnectionStateWaitingForNetwork or ConnectionStateReady or ConnectionStateConnectingToProxy":
        if q.get("@type"):
            return Object.read(q)
        return ConnectionState()
