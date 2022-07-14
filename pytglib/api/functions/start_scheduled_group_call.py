

from ..utils import Object


class StartScheduledGroupCall(Object):
    """
    Starts a scheduled group call 

    Attributes:
        ID (:obj:`str`): ``StartScheduledGroupCall``

    Args:
        group_call_id (:obj:`int`):
            Group call identifier

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "startScheduledGroupCall"

    def __init__(self, group_call_id, extra=None, **kwargs):
        self.extra = extra
        self.group_call_id = group_call_id  # int

    @staticmethod
    def read(q: dict, *args) -> "StartScheduledGroupCall":
        group_call_id = q.get('group_call_id')
        return StartScheduledGroupCall(group_call_id)
