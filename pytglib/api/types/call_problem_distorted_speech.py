

from ..utils import Object


class CallProblemDistortedSpeech(Object):
    """
    The speech was distorted

    Attributes:
        ID (:obj:`str`): ``CallProblemDistortedSpeech``

    No parameters required.

    Returns:
        CallProblem

    Raises:
        :class:`telegram.Error`
    """
    ID = "callProblemDistortedSpeech"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "CallProblemDistortedSpeech":
        
        return CallProblemDistortedSpeech()
