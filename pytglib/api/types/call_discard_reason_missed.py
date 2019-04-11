

from ..utils import Object


class CallDiscardReasonMissed(Object):
    """
    The call was ended before the conversation started. It was cancelled by the caller or missed by the other party

    Attributes:
        ID (:obj:`str`): ``CallDiscardReasonMissed``

    No parameters required.

    Returns:
        CallDiscardReason

    Raises:
        :class:`telegram.Error`
    """
    ID = "callDiscardReasonMissed"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "CallDiscardReasonMissed":
        
        return CallDiscardReasonMissed()
