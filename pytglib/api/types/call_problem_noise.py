

from ..utils import Object


class CallProblemNoise(Object):
    """
    The user heard background noise

    Attributes:
        ID (:obj:`str`): ``CallProblemNoise``

    No parameters required.

    Returns:
        CallProblem

    Raises:
        :class:`telegram.Error`
    """
    ID = "callProblemNoise"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "CallProblemNoise":
        
        return CallProblemNoise()
