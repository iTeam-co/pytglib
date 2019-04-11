

from ..utils import Object


class CallDiscardReasonHungUp(Object):
    """
    The call was ended because one of the parties hung up

    Attributes:
        ID (:obj:`str`): ``CallDiscardReasonHungUp``

    No parameters required.

    Returns:
        CallDiscardReason

    Raises:
        :class:`telegram.Error`
    """
    ID = "callDiscardReasonHungUp"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "CallDiscardReasonHungUp":
        
        return CallDiscardReasonHungUp()
