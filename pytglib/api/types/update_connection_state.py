

from ..utils import Object


class UpdateConnectionState(Object):
    """
    The connection state has changed 

    Attributes:
        ID (:obj:`str`): ``UpdateConnectionState``

    Args:
        state (:class:`telegram.api.types.ConnectionState`):
            The new connection state

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateConnectionState"

    def __init__(self, state, **kwargs):
        
        self.state = state  # ConnectionState

    @staticmethod
    def read(q: dict, *args) -> "UpdateConnectionState":
        state = Object.read(q.get('state'))
        return UpdateConnectionState(state)
