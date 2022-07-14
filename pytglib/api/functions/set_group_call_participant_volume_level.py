

from ..utils import Object


class SetGroupCallParticipantVolumeLevel(Object):
    """
    Changes volume level of a participant of an active group call. If the current user can manage the group call, then the participant's volume level will be changed for all users with the default volume level

    Attributes:
        ID (:obj:`str`): ``SetGroupCallParticipantVolumeLevel``

    Args:
        group_call_id (:obj:`int`):
            Group call identifier 
        participant_id (:class:`telegram.api.types.MessageSender`):
            Participant identifier 
        volume_level (:obj:`int`):
            New participant's volume level; 1-20000 in hundreds of percents

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setGroupCallParticipantVolumeLevel"

    def __init__(self, group_call_id, participant_id, volume_level, extra=None, **kwargs):
        self.extra = extra
        self.group_call_id = group_call_id  # int
        self.participant_id = participant_id  # MessageSender
        self.volume_level = volume_level  # int

    @staticmethod
    def read(q: dict, *args) -> "SetGroupCallParticipantVolumeLevel":
        group_call_id = q.get('group_call_id')
        participant_id = Object.read(q.get('participant_id'))
        volume_level = q.get('volume_level')
        return SetGroupCallParticipantVolumeLevel(group_call_id, participant_id, volume_level)
