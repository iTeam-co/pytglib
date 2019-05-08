

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
    def read(q: dict, *args) -> "CallDiscardReasonHungUp or CallDiscardReasonDisconnected or CallDiscardReasonDeclined or CallDiscardReasonEmpty or CallDiscardReasonMissed":
        if q.get("@type"):
            return Object.read(q)
        return CallDiscardReason()
