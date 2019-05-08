

from ..utils import Object


class MessageSendingState(Object):
    """
    Contains information about the sending state of the message

    No parameters required.
    """
    ID = "messageSendingState"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "MessageSendingStatePending or MessageSendingStateFailed":
        if q.get("@type"):
            return Object.read(q)
        return MessageSendingState()
