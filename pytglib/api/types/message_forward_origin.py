

from ..utils import Object


class MessageForwardOrigin(Object):
    """
    Contains information about the origin of a forwarded message

    No parameters required.
    """
    ID = "messageForwardOrigin"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "MessageForwardOriginChannel or MessageForwardOriginUser or MessageForwardOriginHiddenUser":
        if q.get("@type"):
            return Object.read(q)
        return MessageForwardOrigin()
