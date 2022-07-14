

from ..utils import Object


class ChatEventVideoChatParticipantVolumeLevelChanged(Object):
    """
    A video chat participant volume level was changed 

    Attributes:
        ID (:obj:`str`): ``ChatEventVideoChatParticipantVolumeLevelChanged``

    Args:
        participant_id (:class:`telegram.api.types.MessageSender`):
            Identifier of the affected group call participant 
        volume_level (:obj:`int`):
            New value of volume_level; 1-20000 in hundreds of percents

    Returns:
        ChatEventAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatEventVideoChatParticipantVolumeLevelChanged"

    def __init__(self, participant_id, volume_level, **kwargs):
        
        self.participant_id = participant_id  # MessageSender
        self.volume_level = volume_level  # int

    @staticmethod
    def read(q: dict, *args) -> "ChatEventVideoChatParticipantVolumeLevelChanged":
        participant_id = Object.read(q.get('participant_id'))
        volume_level = q.get('volume_level')
        return ChatEventVideoChatParticipantVolumeLevelChanged(participant_id, volume_level)
