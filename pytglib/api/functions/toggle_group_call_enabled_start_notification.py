

from ..utils import Object


class ToggleGroupCallEnabledStartNotification(Object):
    """
    Toggles whether the current user will receive a notification when the group call will start; scheduled group calls only

    Attributes:
        ID (:obj:`str`): ``ToggleGroupCallEnabledStartNotification``

    Args:
        group_call_id (:obj:`int`):
            Group call identifier 
        enabled_start_notification (:obj:`bool`):
            New value of the enabled_start_notification setting

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "toggleGroupCallEnabledStartNotification"

    def __init__(self, group_call_id, enabled_start_notification, extra=None, **kwargs):
        self.extra = extra
        self.group_call_id = group_call_id  # int
        self.enabled_start_notification = enabled_start_notification  # bool

    @staticmethod
    def read(q: dict, *args) -> "ToggleGroupCallEnabledStartNotification":
        group_call_id = q.get('group_call_id')
        enabled_start_notification = q.get('enabled_start_notification')
        return ToggleGroupCallEnabledStartNotification(group_call_id, enabled_start_notification)
