

from ..utils import Object


class MessageFileType(Object):
    """
    Contains information about a file with messages exported from another app

    No parameters required.
    """
    ID = "messageFileType"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "MessageFileTypeUnknown or MessageFileTypePrivate or MessageFileTypeGroup":
        if q.get("@type"):
            return Object.read(q)
        return MessageFileType()
