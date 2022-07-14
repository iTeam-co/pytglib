

from ..utils import Object


class SetGroupCallParticipantIsSpeaking(Object):
    """
    Informs TDLib that speaking state of a participant of an active group has changed 

    Attributes:
        ID (:obj:`str`): ``SetGroupCallParticipantIsSpeaking``

    Args:
        group_call_id (:obj:`int`):
            Group call identifier
        audio_source (:obj:`int`):
            Group call participant's synchronization audio source identifier, or 0 for the current user 
        is_speaking (:obj:`bool`):
            Pass true if the user is speaking

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setGroupCallParticipantIsSpeaking"

    def __init__(self, group_call_id, audio_source, is_speaking, extra=None, **kwargs):
        self.extra = extra
        self.group_call_id = group_call_id  # int
        self.audio_source = audio_source  # int
        self.is_speaking = is_speaking  # bool

    @staticmethod
    def read(q: dict, *args) -> "SetGroupCallParticipantIsSpeaking":
        group_call_id = q.get('group_call_id')
        audio_source = q.get('audio_source')
        is_speaking = q.get('is_speaking')
        return SetGroupCallParticipantIsSpeaking(group_call_id, audio_source, is_speaking)
