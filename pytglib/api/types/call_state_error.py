

from ..utils import Object


class CallStateError(Object):
    """
    The call has ended with an error 

    Attributes:
        ID (:obj:`str`): ``CallStateError``

    Args:
        error (:class:`telegram.api.types.error`):
            ErrorAn error with the code 4005000 will be returned if an outgoing call is missed because of an expired timeout

    Returns:
        CallState

    Raises:
        :class:`telegram.Error`
    """
    ID = "callStateError"

    def __init__(self, error, **kwargs):
        
        self.error = error  # Error

    @staticmethod
    def read(q: dict, *args) -> "CallStateError":
        error = Object.read(q.get('error'))
        return CallStateError(error)
