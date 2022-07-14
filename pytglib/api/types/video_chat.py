

from ..utils import Object


class VideoChat(Object):
    """
    Describes a video chat

    Attributes:
        ID (:obj:`str`): ``VideoChat``

    Args:
        group_call_id (:obj:`int`):
            Group call identifier of an active video chat; 0 if noneFull information about the video chat can be received through the method getGroupCall
        has_participants (:obj:`bool`):
            True, if the video chat has participants
        default_participant_id (:class:`telegram.api.types.MessageSender`):
            Default group call participant identifier to join the video chat; may be null

    Returns:
        VideoChat

    Raises:
        :class:`telegram.Error`
    """
    ID = "videoChat"

    def __init__(self, group_call_id, has_participants, default_participant_id, **kwargs):
        
        self.group_call_id = group_call_id  # int
        self.has_participants = has_participants  # bool
        self.default_participant_id = default_participant_id  # MessageSender

    @staticmethod
    def read(q: dict, *args) -> "VideoChat":
        group_call_id = q.get('group_call_id')
        has_participants = q.get('has_participants')
        default_participant_id = Object.read(q.get('default_participant_id'))
        return VideoChat(group_call_id, has_participants, default_participant_id)
