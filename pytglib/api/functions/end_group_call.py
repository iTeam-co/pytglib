

from ..utils import Object


class EndGroupCall(Object):
    """
    Ends a group call. Requires groupCall.can_be_managed 

    Attributes:
        ID (:obj:`str`): ``EndGroupCall``

    Args:
        group_call_id (:obj:`int`):
            Group call identifier

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "endGroupCall"

    def __init__(self, group_call_id, extra=None, **kwargs):
        self.extra = extra
        self.group_call_id = group_call_id  # int

    @staticmethod
    def read(q: dict, *args) -> "EndGroupCall":
        group_call_id = q.get('group_call_id')
        return EndGroupCall(group_call_id)
