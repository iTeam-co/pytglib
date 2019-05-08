

from ..utils import Object


class PushReceiverId(Object):
    """
    Contains a globally unique push receiver identifier, which can be used to identify which account has received a push notification 

    Attributes:
        ID (:obj:`str`): ``PushReceiverId``

    Args:
        id (:obj:`int`):
            The globally unique identifier of push notification subscription

    Returns:
        PushReceiverId

    Raises:
        :class:`telegram.Error`
    """
    ID = "pushReceiverId"

    def __init__(self, id, **kwargs):
        
        self.id = id  # int

    @staticmethod
    def read(q: dict, *args) -> "PushReceiverId":
        id = q.get('id')
        return PushReceiverId(id)
