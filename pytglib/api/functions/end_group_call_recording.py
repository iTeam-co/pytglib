

from ..utils import Object


class EndGroupCallRecording(Object):
    """
    Ends recording of an active group call. Requires groupCall.can_be_managed group call flag 

    Attributes:
        ID (:obj:`str`): ``EndGroupCallRecording``

    Args:
        group_call_id (:obj:`int`):
            Group call identifier

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "endGroupCallRecording"

    def __init__(self, group_call_id, extra=None, **kwargs):
        self.extra = extra
        self.group_call_id = group_call_id  # int

    @staticmethod
    def read(q: dict, *args) -> "EndGroupCallRecording":
        group_call_id = q.get('group_call_id')
        return EndGroupCallRecording(group_call_id)
