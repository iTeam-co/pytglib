

from ..utils import Object


class CallState(Object):
    """
    Describes the current call state

    No parameters required.
    """
    ID = "callState"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "CallStatePending or CallStateHangingUp or CallStateDiscarded or CallStateError or CallStateReady or CallStateExchangingKeys":
        if q.get("@type"):
            return Object.read(q)
        return CallState()
