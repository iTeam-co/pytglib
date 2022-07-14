

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
    def read(q: dict, *args) -> "MessageForwardOriginMessageImport or MessageForwardOriginChat or MessageForwardOriginHiddenUser or MessageForwardOriginChannel or MessageForwardOriginUser":
        if q.get("@type"):
            return Object.read(q)
        return MessageForwardOrigin()
