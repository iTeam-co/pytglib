

from ..utils import Object


class MessageSchedulingState(Object):
    """
    Contains information about the time when a scheduled message will be sent

    No parameters required.
    """
    ID = "messageSchedulingState"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "MessageSchedulingStateSendAtDate or MessageSchedulingStateSendWhenOnline":
        if q.get("@type"):
            return Object.read(q)
        return MessageSchedulingState()
