

from ..utils import Object


class MessageForwardInfo(Object):
    """
    Contains information about the initial sender of a forwarded message

    No parameters required.
    """
    ID = "messageForwardInfo"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "MessageForwardedFromUser or MessageForwardedPost":
        if q.get("@type"):
            return Object.read(q)
        return MessageForwardInfo()
