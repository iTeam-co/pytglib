

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
    def read(q: dict, *args) -> "JsonValueArray or JsonValueBoolean or JsonValueObject or JsonValueString or JsonValueNull or JsonValueNumber":
        if q.get("@type"):
            return Object.read(q)
        return JsonValue()
