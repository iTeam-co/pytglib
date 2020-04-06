

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
    def read(q: dict, *args) -> "CallProblemDistortedSpeech or CallProblemNoise or CallProblemDropped or CallProblemSilentRemote or CallProblemEcho or CallProblemInterruptions or CallProblemSilentLocal":
        if q.get("@type"):
            return Object.read(q)
        return CallProblem()
