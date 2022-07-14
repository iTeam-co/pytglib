

from ..utils import Object


class MessageVideoChatScheduled(Object):
    """
    A new video chat was scheduled 

    Attributes:
        ID (:obj:`str`): ``MessageVideoChatScheduled``

    Args:
        group_call_id (:obj:`int`):
            Identifier of the video chatThe video chat can be received through the method getGroupCall 
        start_date (:obj:`int`):
            Point in time (Unix timestamp) when the group call is supposed to be started by an administrator

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageVideoChatScheduled"

    def __init__(self, group_call_id, start_date, **kwargs):
        
        self.group_call_id = group_call_id  # int
        self.start_date = start_date  # int

    @staticmethod
    def read(q: dict, *args) -> "MessageVideoChatScheduled":
        group_call_id = q.get('group_call_id')
        start_date = q.get('start_date')
        return MessageVideoChatScheduled(group_call_id, start_date)
