

from ..utils import Object


class ConnectionStateReady(Object):
    """
    There is a working connection to the Telegram servers

    Attributes:
        ID (:obj:`str`): ``ConnectionStateReady``

    No parameters required.

    Returns:
        ConnectionState

    Raises:
        :class:`telegram.Error`
    """
    ID = "connectionStateReady"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ConnectionStateReady":
        
        return ConnectionStateReady()
