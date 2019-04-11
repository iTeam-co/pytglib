

from ..utils import Object


class DiscardCall(Object):
    """
    Discards a call 

    Attributes:
        ID (:obj:`str`): ``DiscardCall``

    Args:
        call_id (:obj:`int`):
            Call identifier 
        is_disconnected (:obj:`bool`):
            True, if the user was disconnected 
        duration (:obj:`int`):
            The call duration, in seconds 
        connection_id (:obj:`int`):
            Identifier of the connection used during the call

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "discardCall"

    def __init__(self, call_id, is_disconnected, duration, connection_id, extra=None, **kwargs):
        self.extra = extra
        self.call_id = call_id  # int
        self.is_disconnected = is_disconnected  # bool
        self.duration = duration  # int
        self.connection_id = connection_id  # int

    @staticmethod
    def read(q: dict, *args) -> "DiscardCall":
        call_id = q.get('call_id')
        is_disconnected = q.get('is_disconnected')
        duration = q.get('duration')
        connection_id = q.get('connection_id')
        return DiscardCall(call_id, is_disconnected, duration, connection_id)
