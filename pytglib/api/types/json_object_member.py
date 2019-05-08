

from ..utils import Object


class JsonObjectMember(Object):
    """
    Represents one member of a JSON object 

    Attributes:
        ID (:obj:`str`): ``JsonObjectMember``

    Args:
        key (:obj:`str`):
            Member's key 
        value (:class:`telegram.api.types.JsonValue`):
            Member's value

    Returns:
        JsonObjectMember

    Raises:
        :class:`telegram.Error`
    """
    ID = "jsonObjectMember"

    def __init__(self, key, value, **kwargs):
        
        self.key = key  # str
        self.value = value  # JsonValue

    @staticmethod
    def read(q: dict, *args) -> "JsonObjectMember":
        key = q.get('key')
        value = Object.read(q.get('value'))
        return JsonObjectMember(key, value)
