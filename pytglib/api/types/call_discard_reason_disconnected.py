

from ..utils import Object


class CallDiscardReasonDisconnected(Object):
    """
    The call was ended during the conversation because the users were disconnected

    Attributes:
        ID (:obj:`str`): ``CallDiscardReasonDisconnected``

    No parameters required.

    Returns:
        CallDiscardReason

    Raises:
        :class:`telegram.Error`
    """
    ID = "callDiscardReasonDisconnected"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "CallDiscardReasonDisconnected":
        
        return CallDiscardReasonDisconnected()
