

from ..utils import Object


class JsonValueString(Object):
    """
    Represents a string JSON value 

    Attributes:
        ID (:obj:`str`): ``JsonValueString``

    Args:
        value (:obj:`str`):
            The value

    Returns:
        JsonValue

    Raises:
        :class:`telegram.Error`
    """
    ID = "jsonValueString"

    def __init__(self, value, **kwargs):
        
        self.value = value  # str

    @staticmethod
    def read(q: dict, *args) -> "JsonValueString":
        value = q.get('value')
        return JsonValueString(value)
