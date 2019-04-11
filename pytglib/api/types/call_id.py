

from ..utils import Object


class CallId(Object):
    """
    Contains the call identifier 

    Attributes:
        ID (:obj:`str`): ``CallId``

    Args:
        id (:obj:`int`):
            Call identifier

    Returns:
        CallId

    Raises:
        :class:`telegram.Error`
    """
    ID = "callId"

    def __init__(self, id, **kwargs):
        
        self.id = id  # int

    @staticmethod
    def read(q: dict, *args) -> "CallId":
        id = q.get('id')
        return CallId(id)
