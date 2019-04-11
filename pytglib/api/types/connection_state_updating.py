

from ..utils import Object


class ConnectionStateUpdating(Object):
    """
    Downloading data received while the client was offline

    Attributes:
        ID (:obj:`str`): ``ConnectionStateUpdating``

    No parameters required.

    Returns:
        ConnectionState

    Raises:
        :class:`telegram.Error`
    """
    ID = "connectionStateUpdating"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ConnectionStateUpdating":
        
        return ConnectionStateUpdating()
