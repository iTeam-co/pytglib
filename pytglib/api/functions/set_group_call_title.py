

from ..utils import Object


class SetGroupCallTitle(Object):
    """
    Sets group call title. Requires groupCall.can_be_managed group call flag 

    Attributes:
        ID (:obj:`str`): ``SetGroupCallTitle``

    Args:
        group_call_id (:obj:`int`):
            Group call identifier 
        title (:obj:`str`):
            New group call title; 1-64 characters

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setGroupCallTitle"

    def __init__(self, group_call_id, title, extra=None, **kwargs):
        self.extra = extra
        self.group_call_id = group_call_id  # int
        self.title = title  # str

    @staticmethod
    def read(q: dict, *args) -> "SetGroupCallTitle":
        group_call_id = q.get('group_call_id')
        title = q.get('title')
        return SetGroupCallTitle(group_call_id, title)
