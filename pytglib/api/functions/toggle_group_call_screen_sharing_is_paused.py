

from ..utils import Object


class ToggleGroupCallScreenSharingIsPaused(Object):
    """
    Pauses or unpauses screen sharing in a joined group call 

    Attributes:
        ID (:obj:`str`): ``ToggleGroupCallScreenSharingIsPaused``

    Args:
        group_call_id (:obj:`int`):
            Group call identifier 
        is_paused (:obj:`bool`):
            True if screen sharing is paused

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "toggleGroupCallScreenSharingIsPaused"

    def __init__(self, group_call_id, is_paused, extra=None, **kwargs):
        self.extra = extra
        self.group_call_id = group_call_id  # int
        self.is_paused = is_paused  # bool

    @staticmethod
    def read(q: dict, *args) -> "ToggleGroupCallScreenSharingIsPaused":
        group_call_id = q.get('group_call_id')
        is_paused = q.get('is_paused')
        return ToggleGroupCallScreenSharingIsPaused(group_call_id, is_paused)
