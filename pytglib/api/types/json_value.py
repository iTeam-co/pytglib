

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
    def read(q: dict, *args) -> "JsonValueString or JsonValueBoolean or JsonValueNull or JsonValueArray or JsonValueNumber or JsonValueObject":
        if q.get("@type"):
            return Object.read(q)
        return JsonValue()
