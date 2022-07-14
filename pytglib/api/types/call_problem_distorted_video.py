

from ..utils import Object


class CallProblemDistortedVideo(Object):
    """
    The video was distorted

    Attributes:
        ID (:obj:`str`): ``CallProblemDistortedVideo``

    No parameters required.

    Returns:
        CallProblem

    Raises:
        :class:`telegram.Error`
    """
    ID = "callProblemDistortedVideo"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "CallProblemDistortedVideo":
        
        return CallProblemDistortedVideo()
