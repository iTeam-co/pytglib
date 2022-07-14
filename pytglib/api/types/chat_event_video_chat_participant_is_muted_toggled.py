

from ..utils import Object


class ChatEventVideoChatParticipantIsMutedToggled(Object):
    """
    A video chat participant was muted or unmuted 

    Attributes:
        ID (:obj:`str`): ``ChatEventVideoChatParticipantIsMutedToggled``

    Args:
        participant_id (:class:`telegram.api.types.MessageSender`):
            Identifier of the affected group call participant 
        is_muted (:obj:`bool`):
            New value of is_muted

    Returns:
        ChatEventAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatEventVideoChatParticipantIsMutedToggled"

    def __init__(self, participant_id, is_muted, **kwargs):
        
        self.participant_id = participant_id  # MessageSender
        self.is_muted = is_muted  # bool

    @staticmethod
    def read(q: dict, *args) -> "ChatEventVideoChatParticipantIsMutedToggled":
        participant_id = Object.read(q.get('participant_id'))
        is_muted = q.get('is_muted')
        return ChatEventVideoChatParticipantIsMutedToggled(participant_id, is_muted)
