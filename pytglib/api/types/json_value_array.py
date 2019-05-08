

from ..utils import Object


class JsonValueArray(Object):
    """
    Represents a JSON array 

    Attributes:
        ID (:obj:`str`): ``JsonValueArray``

    Args:
        values (List of :class:`telegram.api.types.JsonValue`):
            The list of array elements

    Returns:
        JsonValue

    Raises:
        :class:`telegram.Error`
    """
    ID = "jsonValueArray"

    def __init__(self, values, **kwargs):
        
        self.values = values  # list of JsonValue

    @staticmethod
    def read(q: dict, *args) -> "JsonValueArray":
        values = [Object.read(i) for i in q.get('values', [])]
        return JsonValueArray(values)
