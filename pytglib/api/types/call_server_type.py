

from ..utils import Object


class CallServerType(Object):
    """
    Describes the type of a call server

    No parameters required.
    """
    ID = "callServerType"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "CallServerTypeWebrtc or CallServerTypeTelegramReflector":
        if q.get("@type"):
            return Object.read(q)
        return CallServerType()
