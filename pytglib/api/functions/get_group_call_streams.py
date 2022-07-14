

from ..utils import Object


class GetGroupCallStreams(Object):
    """
    Returns information about available group call streams 

    Attributes:
        ID (:obj:`str`): ``GetGroupCallStreams``

    Args:
        group_call_id (:obj:`int`):
            Group call identifier

    Returns:
        GroupCallStreams

    Raises:
        :class:`telegram.Error`
    """
    ID = "getGroupCallStreams"

    def __init__(self, group_call_id, extra=None, **kwargs):
        self.extra = extra
        self.group_call_id = group_call_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetGroupCallStreams":
        group_call_id = q.get('group_call_id')
        return GetGroupCallStreams(group_call_id)
