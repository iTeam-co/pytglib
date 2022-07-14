

from ..utils import Object


class GroupCallId(Object):
    """
    Contains the group call identifier 

    Attributes:
        ID (:obj:`str`): ``GroupCallId``

    Args:
        id (:obj:`int`):
            Group call identifier

    Returns:
        GroupCallId

    Raises:
        :class:`telegram.Error`
    """
    ID = "groupCallId"

    def __init__(self, id, **kwargs):
        
        self.id = id  # int

    @staticmethod
    def read(q: dict, *args) -> "GroupCallId":
        id = q.get('id')
        return GroupCallId(id)
