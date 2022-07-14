

from ..utils import Object


class StartGroupCallRecording(Object):
    """
    Starts recording of an active group call. Requires groupCall.can_be_managed group call flag 

    Attributes:
        ID (:obj:`str`): ``StartGroupCallRecording``

    Args:
        group_call_id (:obj:`int`):
            Group call identifier 
        title (:obj:`str`):
            Group call recording title; 0-64 characters
        record_video (:obj:`bool`):
            Pass true to record a video file instead of an audio file 
        use_portrait_orientation (:obj:`bool`):
            Pass true to use portrait orientation for video instead of landscape one

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "startGroupCallRecording"

    def __init__(self, group_call_id, title, record_video, use_portrait_orientation, extra=None, **kwargs):
        self.extra = extra
        self.group_call_id = group_call_id  # int
        self.title = title  # str
        self.record_video = record_video  # bool
        self.use_portrait_orientation = use_portrait_orientation  # bool

    @staticmethod
    def read(q: dict, *args) -> "StartGroupCallRecording":
        group_call_id = q.get('group_call_id')
        title = q.get('title')
        record_video = q.get('record_video')
        use_portrait_orientation = q.get('use_portrait_orientation')
        return StartGroupCallRecording(group_call_id, title, record_video, use_portrait_orientation)
