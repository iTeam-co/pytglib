

from ..utils import Object


class CallProblem(Object):
    """
    Describes the exact type of a problem with a call

    No parameters required.
    """
    ID = "callProblem"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "CallProblemDropped or CallProblemPixelatedVideo or CallProblemEcho or CallProblemSilentLocal or CallProblemDistortedSpeech or CallProblemInterruptions or CallProblemSilentRemote or CallProblemDistortedVideo or CallProblemNoise":
        if q.get("@type"):
            return Object.read(q)
        return CallProblem()
