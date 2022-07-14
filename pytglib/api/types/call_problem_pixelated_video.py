

from ..utils import Object


class CallProblemPixelatedVideo(Object):
    """
    The video was pixelated

    Attributes:
        ID (:obj:`str`): ``CallProblemPixelatedVideo``

    No parameters required.

    Returns:
        CallProblem

    Raises:
        :class:`telegram.Error`
    """
    ID = "callProblemPixelatedVideo"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "CallProblemPixelatedVideo":
        
        return CallProblemPixelatedVideo()
