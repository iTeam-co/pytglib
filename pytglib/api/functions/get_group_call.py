

from ..utils import Object


class GetGroupCall(Object):
    """
    Returns information about a group call 

    Attributes:
        ID (:obj:`str`): ``GetGroupCall``

    Args:
        group_call_id (:obj:`int`):
            Group call identifier

    Returns:
        GroupCall

    Raises:
        :class:`telegram.Error`
    """
    ID = "getGroupCall"

    def __init__(self, group_call_id, extra=None, **kwargs):
        self.extra = extra
        self.group_call_id = group_call_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetGroupCall":
        group_call_id = q.get('group_call_id')
        return GetGroupCall(group_call_id)
