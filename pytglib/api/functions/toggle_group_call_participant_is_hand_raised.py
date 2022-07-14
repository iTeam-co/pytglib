

from ..utils import Object


class ToggleGroupCallParticipantIsHandRaised(Object):
    """
    Toggles whether a group call participant hand is rased

    Attributes:
        ID (:obj:`str`): ``ToggleGroupCallParticipantIsHandRaised``

    Args:
        group_call_id (:obj:`int`):
            Group call identifier 
        participant_id (:class:`telegram.api.types.MessageSender`):
            Participant identifier
        is_hand_raised (:obj:`bool`):
            Pass true if the user's hand needs to be raisedOnly self hand can be raisedRequires groupCallcan_be_managed group call flag to lower other's hand

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "toggleGroupCallParticipantIsHandRaised"

    def __init__(self, group_call_id, participant_id, is_hand_raised, extra=None, **kwargs):
        self.extra = extra
        self.group_call_id = group_call_id  # int
        self.participant_id = participant_id  # MessageSender
        self.is_hand_raised = is_hand_raised  # bool

    @staticmethod
    def read(q: dict, *args) -> "ToggleGroupCallParticipantIsHandRaised":
        group_call_id = q.get('group_call_id')
        participant_id = Object.read(q.get('participant_id'))
        is_hand_raised = q.get('is_hand_raised')
        return ToggleGroupCallParticipantIsHandRaised(group_call_id, participant_id, is_hand_raised)
