

from ..utils import Object


class EndGroupCallScreenSharing(Object):
    """
    Ends screen sharing in a joined group call 

    Attributes:
        ID (:obj:`str`): ``EndGroupCallScreenSharing``

    Args:
        group_call_id (:obj:`int`):
            Group call identifier

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "endGroupCallScreenSharing"

    def __init__(self, group_call_id, extra=None, **kwargs):
        self.extra = extra
        self.group_call_id = group_call_id  # int

    @staticmethod
    def read(q: dict, *args) -> "EndGroupCallScreenSharing":
        group_call_id = q.get('group_call_id')
        return EndGroupCallScreenSharing(group_call_id)
