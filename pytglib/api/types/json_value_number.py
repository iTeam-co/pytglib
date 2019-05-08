

from ..utils import Object


class JsonValueNumber(Object):
    """
    Represents a numeric JSON value 

    Attributes:
        ID (:obj:`str`): ``JsonValueNumber``

    Args:
        value (:obj:`float`):
            The value

    Returns:
        JsonValue

    Raises:
        :class:`telegram.Error`
    """
    ID = "jsonValueNumber"

    def __init__(self, value, **kwargs):
        
        self.value = value  # float

    @staticmethod
    def read(q: dict, *args) -> "JsonValueNumber":
        value = q.get('value')
        return JsonValueNumber(value)
