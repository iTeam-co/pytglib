

from ..utils import Object


class JsonValueBoolean(Object):
    """
    Represents a boolean JSON value 

    Attributes:
        ID (:obj:`str`): ``JsonValueBoolean``

    Args:
        value (:obj:`bool`):
            The value

    Returns:
        JsonValue

    Raises:
        :class:`telegram.Error`
    """
    ID = "jsonValueBoolean"

    def __init__(self, value, **kwargs):
        
        self.value = value  # bool

    @staticmethod
    def read(q: dict, *args) -> "JsonValueBoolean":
        value = q.get('value')
        return JsonValueBoolean(value)
