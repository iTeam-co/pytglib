

from ..utils import Object


class CallbackQueryPayload(Object):
    """
    Represents a payload of a callback query

    No parameters required.
    """
    ID = "callbackQueryPayload"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "CallbackQueryPayloadData or CallbackQueryPayloadDataWithPassword or CallbackQueryPayloadGame":
        if q.get("@type"):
            return Object.read(q)
        return CallbackQueryPayload()
