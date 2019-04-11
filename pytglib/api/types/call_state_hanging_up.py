

from ..utils import Object


class CallStateHangingUp(Object):
    """
    The call is hanging up after discardCall has been called

    Attributes:
        ID (:obj:`str`): ``CallStateHangingUp``

    No parameters required.

    Returns:
        CallState

    Raises:
        :class:`telegram.Error`
    """
    ID = "callStateHangingUp"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "CallStateHangingUp":
        
        return CallStateHangingUp()
