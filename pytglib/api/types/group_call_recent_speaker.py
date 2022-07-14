

from ..utils import Object


class GroupCallRecentSpeaker(Object):
    """
    Describes a recently speaking participant in a group call 

    Attributes:
        ID (:obj:`str`): ``GroupCallRecentSpeaker``

    Args:
        participant_id (:class:`telegram.api.types.MessageSender`):
            Group call participant identifier 
        is_speaking (:obj:`bool`):
            True, is the user has spoken recently

    Returns:
        GroupCallRecentSpeaker

    Raises:
        :class:`telegram.Error`
    """
    ID = "groupCallRecentSpeaker"

    def __init__(self, participant_id, is_speaking, **kwargs):
        
        self.participant_id = participant_id  # MessageSender
        self.is_speaking = is_speaking  # bool

    @staticmethod
    def read(q: dict, *args) -> "GroupCallRecentSpeaker":
        participant_id = Object.read(q.get('participant_id'))
        is_speaking = q.get('is_speaking')
        return GroupCallRecentSpeaker(participant_id, is_speaking)
