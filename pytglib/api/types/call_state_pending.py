

from ..utils import Object


class CallStatePending(Object):
    """
    The call is pending, waiting to be accepted by a user 

    Attributes:
        ID (:obj:`str`): ``CallStatePending``

    Args:
        is_created (:obj:`bool`):
            True, if the call has already been created by the server 
        is_received (:obj:`bool`):
            True, if the call has already been received by the other party

    Returns:
        CallState

    Raises:
        :class:`telegram.Error`
    """
    ID = "callStatePending"

    def __init__(self, is_created, is_received, **kwargs):
        
        self.is_created = is_created  # bool
        self.is_received = is_received  # bool

    @staticmethod
    def read(q: dict, *args) -> "CallStatePending":
        is_created = q.get('is_created')
        is_received = q.get('is_received')
        return CallStatePending(is_created, is_received)
