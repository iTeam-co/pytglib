

from ..utils import Object


class CallProblemDropped(Object):
    """
    The call ended unexpectedly

    Attributes:
        ID (:obj:`str`): ``CallProblemDropped``

    No parameters required.

    Returns:
        CallProblem

    Raises:
        :class:`telegram.Error`
    """
    ID = "callProblemDropped"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "CallProblemDropped":
        
        return CallProblemDropped()
