

from ..utils import Object


class ToggleGroupCallIsMyVideoPaused(Object):
    """
    Toggles whether current user's video is paused 

    Attributes:
        ID (:obj:`str`): ``ToggleGroupCallIsMyVideoPaused``

    Args:
        group_call_id (:obj:`int`):
            Group call identifier 
        is_my_video_paused (:obj:`bool`):
            Pass true if the current user's video is paused

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "toggleGroupCallIsMyVideoPaused"

    def __init__(self, group_call_id, is_my_video_paused, extra=None, **kwargs):
        self.extra = extra
        self.group_call_id = group_call_id  # int
        self.is_my_video_paused = is_my_video_paused  # bool

    @staticmethod
    def read(q: dict, *args) -> "ToggleGroupCallIsMyVideoPaused":
        group_call_id = q.get('group_call_id')
        is_my_video_paused = q.get('is_my_video_paused')
        return ToggleGroupCallIsMyVideoPaused(group_call_id, is_my_video_paused)
