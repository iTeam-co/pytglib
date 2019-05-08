

from ..utils import Object


class JsonValue(Object):
    """
    Represents a JSON value

    No parameters required.
    """
    ID = "jsonValue"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "JsonValueNull or JsonValueArray or JsonValueNumber or JsonValueString or JsonValueObject or JsonValueBoolean":
        if q.get("@type"):
            return Object.read(q)
        return JsonValue()
