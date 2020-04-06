

from ..utils import Object


class CallDiscardReason(Object):
    """
    Describes the reason why a call was discarded

    No parameters required.
    """
    ID = "callDiscardReason"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "CallDiscardReasonDisconnected or CallDiscardReasonHungUp or CallDiscardReasonEmpty or CallDiscardReasonDeclined or CallDiscardReasonMissed":
        if q.get("@type"):
            return Object.read(q)
        return CallDiscardReason()
