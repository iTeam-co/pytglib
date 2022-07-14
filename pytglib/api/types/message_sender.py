

from ..utils import Object


class MessageSender(Object):
    """
    Contains information about the sender of a message

    No parameters required.
    """
    ID = "messageSender"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "MessageSenderChat or MessageSenderUser":
        if q.get("@type"):
            return Object.read(q)
        return MessageSender()
