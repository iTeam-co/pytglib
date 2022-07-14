

from ..utils import Object


class GroupCallParticipantVideoInfo(Object):
    """
    Contains information about a group call participant's video channel 

    Attributes:
        ID (:obj:`str`): ``GroupCallParticipantVideoInfo``

    Args:
        source_groups (List of :class:`telegram.api.types.groupCallVideoSourceGroup`):
            List of synchronization source groups of the video 
        endpoint_id (:obj:`str`):
            Video channel endpoint identifier
        is_paused (:obj:`bool`):
            True if the video is pausedThis flag needs to be ignored, if new video frames are received

    Returns:
        GroupCallParticipantVideoInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "groupCallParticipantVideoInfo"

    def __init__(self, source_groups, endpoint_id, is_paused, **kwargs):
        
        self.source_groups = source_groups  # list of groupCallVideoSourceGroup
        self.endpoint_id = endpoint_id  # str
        self.is_paused = is_paused  # bool

    @staticmethod
    def read(q: dict, *args) -> "GroupCallParticipantVideoInfo":
        source_groups = [Object.read(i) for i in q.get('source_groups', [])]
        endpoint_id = q.get('endpoint_id')
        is_paused = q.get('is_paused')
        return GroupCallParticipantVideoInfo(source_groups, endpoint_id, is_paused)
