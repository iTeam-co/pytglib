

from ..utils import Object


class GetJsonValue(Object):
    """
    Converts a JSON-serialized string to corresponding JsonValue object. This is an offline method. Can be called before authorization. Can be called synchronously 

    Attributes:
        ID (:obj:`str`): ``GetJsonValue``

    Args:
        json (:obj:`str`):
            The JSON-serialized string

    Returns:
        JsonValue

    Raises:
        :class:`telegram.Error`
    """
    ID = "getJsonValue"

    def __init__(self, json, extra=None, **kwargs):
        self.extra = extra
        self.json = json  # str

    @staticmethod
    def read(q: dict, *args) -> "GetJsonValue":
        json = q.get('json')
        return GetJsonValue(json)
