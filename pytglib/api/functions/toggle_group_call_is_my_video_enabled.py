

from ..utils import Object


class ToggleGroupCallIsMyVideoEnabled(Object):
    """
    Toggles whether current user's video is enabled 

    Attributes:
        ID (:obj:`str`): ``ToggleGroupCallIsMyVideoEnabled``

    Args:
        group_call_id (:obj:`int`):
            Group call identifier 
        is_my_video_enabled (:obj:`bool`):
            Pass true if the current user's video is enabled

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "toggleGroupCallIsMyVideoEnabled"

    def __init__(self, group_call_id, is_my_video_enabled, extra=None, **kwargs):
        self.extra = extra
        self.group_call_id = group_call_id  # int
        self.is_my_video_enabled = is_my_video_enabled  # bool

    @staticmethod
    def read(q: dict, *args) -> "ToggleGroupCallIsMyVideoEnabled":
        group_call_id = q.get('group_call_id')
        is_my_video_enabled = q.get('is_my_video_enabled')
        return ToggleGroupCallIsMyVideoEnabled(group_call_id, is_my_video_enabled)
