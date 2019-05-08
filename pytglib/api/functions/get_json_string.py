

from ..utils import Object


class GetJsonString(Object):
    """
    Converts a JsonValue object to corresponding JSON-serialized string. This is an offline method. Can be called before authorization. Can be called synchronously 

    Attributes:
        ID (:obj:`str`): ``GetJsonString``

    Args:
        json_value (:class:`telegram.api.types.JsonValue`):
            The JsonValue object

    Returns:
        Text

    Raises:
        :class:`telegram.Error`
    """
    ID = "getJsonString"

    def __init__(self, json_value, extra=None, **kwargs):
        self.extra = extra
        self.json_value = json_value  # JsonValue

    @staticmethod
    def read(q: dict, *args) -> "GetJsonString":
        json_value = Object.read(q.get('json_value'))
        return GetJsonString(json_value)
