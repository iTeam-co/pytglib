

from ..utils import Object


class CallDiscardReasonEmpty(Object):
    """
    The call wasn't discarded, or the reason is unknown

    Attributes:
        ID (:obj:`str`): ``CallDiscardReasonEmpty``

    No parameters required.

    Returns:
        CallDiscardReason

    Raises:
        :class:`telegram.Error`
    """
    ID = "callDiscardReasonEmpty"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "CallDiscardReasonEmpty":
        
        return CallDiscardReasonEmpty()
