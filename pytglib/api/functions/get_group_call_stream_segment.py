

from ..utils import Object


class GetGroupCallStreamSegment(Object):
    """
    Returns a file with a segment of a group call stream in a modified OGG format for audio or MPEG-4 format for video

    Attributes:
        ID (:obj:`str`): ``GetGroupCallStreamSegment``

    Args:
        group_call_id (:obj:`int`):
            Group call identifier
        time_offset (:obj:`int`):
            Point in time when the stream segment begins; Unix timestamp in milliseconds
        scale (:obj:`int`):
            Segment duration scale; 0-1Segment's duration is 1000/(2**scale) milliseconds
        channel_id (:obj:`int`):
            Identifier of an audio/video channel to get as received from tgcalls
        video_quality (:class:`telegram.api.types.GroupCallVideoQuality`):
            Video quality as received from tgcalls; pass null to get the worst available quality

    Returns:
        FilePart

    Raises:
        :class:`telegram.Error`
    """
    ID = "getGroupCallStreamSegment"

    def __init__(self, group_call_id, time_offset, scale, channel_id, video_quality, extra=None, **kwargs):
        self.extra = extra
        self.group_call_id = group_call_id  # int
        self.time_offset = time_offset  # int
        self.scale = scale  # int
        self.channel_id = channel_id  # int
        self.video_quality = video_quality  # GroupCallVideoQuality

    @staticmethod
    def read(q: dict, *args) -> "GetGroupCallStreamSegment":
        group_call_id = q.get('group_call_id')
        time_offset = q.get('time_offset')
        scale = q.get('scale')
        channel_id = q.get('channel_id')
        video_quality = Object.read(q.get('video_quality'))
        return GetGroupCallStreamSegment(group_call_id, time_offset, scale, channel_id, video_quality)
