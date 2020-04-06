

from ..utils import Object


class CallProblemSilentRemote(Object):
    """
    The other side couldn't hear the user

    Attributes:
        ID (:obj:`str`): ``CallProblemSilentRemote``

    No parameters required.

    Returns:
        CallProblem

    Raises:
        :class:`telegram.Error`
    """
    ID = "callProblemSilentRemote"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "CallProblemSilentRemote":
        
        return CallProblemSilentRemote()
