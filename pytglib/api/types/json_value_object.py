

from ..utils import Object


class JsonValueObject(Object):
    """
    Represents a JSON object 

    Attributes:
        ID (:obj:`str`): ``JsonValueObject``

    Args:
        members (List of :class:`telegram.api.types.jsonObjectMember`):
            The list of object members

    Returns:
        JsonValue

    Raises:
        :class:`telegram.Error`
    """
    ID = "jsonValueObject"

    def __init__(self, members, **kwargs):
        
        self.members = members  # list of jsonObjectMember

    @staticmethod
    def read(q: dict, *args) -> "JsonValueObject":
        members = [Object.read(i) for i in q.get('members', [])]
        return JsonValueObject(members)
