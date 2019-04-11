

from ..utils import Object


class CallDiscardReasonDeclined(Object):
    """
    The call was ended before the conversation started. It was declined by the other party

    Attributes:
        ID (:obj:`str`): ``CallDiscardReasonDeclined``

    No parameters required.

    Returns:
        CallDiscardReason

    Raises:
        :class:`telegram.Error`
    """
    ID = "callDiscardReasonDeclined"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "CallDiscardReasonDeclined":
        
        return CallDiscardReasonDeclined()
