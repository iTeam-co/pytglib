

from ..utils import Object


class LeaveGroupCall(Object):
    """
    Leaves a group call 

    Attributes:
        ID (:obj:`str`): ``LeaveGroupCall``

    Args:
        group_call_id (:obj:`int`):
            Group call identifier

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "leaveGroupCall"

    def __init__(self, group_call_id, extra=None, **kwargs):
        self.extra = extra
        self.group_call_id = group_call_id  # int

    @staticmethod
    def read(q: dict, *args) -> "LeaveGroupCall":
        group_call_id = q.get('group_call_id')
        return LeaveGroupCall(group_call_id)
