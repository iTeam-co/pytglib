

from ..utils import Object


class UpdateGroupCallParticipant(Object):
    """
    Information about a group call participant was changed. The updates are sent only after the group call is received through getGroupCall and only if the call is joined or being joined

    Attributes:
        ID (:obj:`str`): ``UpdateGroupCallParticipant``

    Args:
        group_call_id (:obj:`int`):
            Identifier of group call 
        participant (:class:`telegram.api.types.groupCallParticipant`):
            New data about a participant

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateGroupCallParticipant"

    def __init__(self, group_call_id, participant, **kwargs):
        
        self.group_call_id = group_call_id  # int
        self.participant = participant  # GroupCallParticipant

    @staticmethod
    def read(q: dict, *args) -> "UpdateGroupCallParticipant":
        group_call_id = q.get('group_call_id')
        participant = Object.read(q.get('participant'))
        return UpdateGroupCallParticipant(group_call_id, participant)
