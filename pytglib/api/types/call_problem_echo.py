

from ..utils import Object


class CallProblemEcho(Object):
    """
    The user heard their own voice

    Attributes:
        ID (:obj:`str`): ``CallProblemEcho``

    No parameters required.

    Returns:
        CallProblem

    Raises:
        :class:`telegram.Error`
    """
    ID = "callProblemEcho"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "CallProblemEcho":
        
        return CallProblemEcho()
