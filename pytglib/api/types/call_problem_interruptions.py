

from ..utils import Object


class CallProblemInterruptions(Object):
    """
    The other side kept disappearing

    Attributes:
        ID (:obj:`str`): ``CallProblemInterruptions``

    No parameters required.

    Returns:
        CallProblem

    Raises:
        :class:`telegram.Error`
    """
    ID = "callProblemInterruptions"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "CallProblemInterruptions":
        
        return CallProblemInterruptions()
