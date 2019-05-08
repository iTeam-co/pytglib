

from ..utils import Object


class JsonValueNull(Object):
    """
    Represents a null JSON value

    Attributes:
        ID (:obj:`str`): ``JsonValueNull``

    No parameters required.

    Returns:
        JsonValue

    Raises:
        :class:`telegram.Error`
    """
    ID = "jsonValueNull"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "JsonValueNull":
        
        return JsonValueNull()
