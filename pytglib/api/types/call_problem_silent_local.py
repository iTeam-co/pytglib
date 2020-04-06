

from ..utils import Object


class CallProblemSilentLocal(Object):
    """
    The user couldn't hear the other side

    Attributes:
        ID (:obj:`str`): ``CallProblemSilentLocal``

    No parameters required.

    Returns:
        CallProblem

    Raises:
        :class:`telegram.Error`
    """
    ID = "callProblemSilentLocal"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "CallProblemSilentLocal":
        
        return CallProblemSilentLocal()
