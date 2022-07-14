

from ..utils import Object


class ToggleGroupCallMuteNewParticipants(Object):
    """
    Toggles whether new participants of a group call can be unmuted only by administrators of the group call. Requires groupCall.can_toggle_mute_new_participants group call flag

    Attributes:
        ID (:obj:`str`): ``ToggleGroupCallMuteNewParticipants``

    Args:
        group_call_id (:obj:`int`):
            Group call identifier 
        mute_new_participants (:obj:`bool`):
            New value of the mute_new_participants setting

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "toggleGroupCallMuteNewParticipants"

    def __init__(self, group_call_id, mute_new_participants, extra=None, **kwargs):
        self.extra = extra
        self.group_call_id = group_call_id  # int
        self.mute_new_participants = mute_new_participants  # bool

    @staticmethod
    def read(q: dict, *args) -> "ToggleGroupCallMuteNewParticipants":
        group_call_id = q.get('group_call_id')
        mute_new_participants = q.get('mute_new_participants')
        return ToggleGroupCallMuteNewParticipants(group_call_id, mute_new_participants)
