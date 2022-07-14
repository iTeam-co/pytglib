

from ..utils import Object


class ToggleGroupCallParticipantIsMuted(Object):
    """
    Toggles whether a participant of an active group call is muted, unmuted, or allowed to unmute themselves

    Attributes:
        ID (:obj:`str`): ``ToggleGroupCallParticipantIsMuted``

    Args:
        group_call_id (:obj:`int`):
            Group call identifier 
        participant_id (:class:`telegram.api.types.MessageSender`):
            Participant identifier 
        is_muted (:obj:`bool`):
            Pass true to mute the user; pass false to unmute the them

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "toggleGroupCallParticipantIsMuted"

    def __init__(self, group_call_id, participant_id, is_muted, extra=None, **kwargs):
        self.extra = extra
        self.group_call_id = group_call_id  # int
        self.participant_id = participant_id  # MessageSender
        self.is_muted = is_muted  # bool

    @staticmethod
    def read(q: dict, *args) -> "ToggleGroupCallParticipantIsMuted":
        group_call_id = q.get('group_call_id')
        participant_id = Object.read(q.get('participant_id'))
        is_muted = q.get('is_muted')
        return ToggleGroupCallParticipantIsMuted(group_call_id, participant_id, is_muted)
