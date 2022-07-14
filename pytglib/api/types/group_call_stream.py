

from ..utils import Object


class GroupCallStream(Object):
    """
    Describes an available stream in a group call

    Attributes:
        ID (:obj:`str`): ``GroupCallStream``

    Args:
        channel_id (:obj:`int`):
            Identifier of an audio/video channel
        scale (:obj:`int`):
            Scale of segment durations in the streamThe duration is 1000/(2**scale) milliseconds
        time_offset (:obj:`int`):
            Point in time when the stream currently ends; Unix timestamp in milliseconds

    Returns:
        GroupCallStream

    Raises:
        :class:`telegram.Error`
    """
    ID = "groupCallStream"

    def __init__(self, channel_id, scale, time_offset, **kwargs):
        
        self.channel_id = channel_id  # int
        self.scale = scale  # int
        self.time_offset = time_offset  # int

    @staticmethod
    def read(q: dict, *args) -> "GroupCallStream":
        channel_id = q.get('channel_id')
        scale = q.get('scale')
        time_offset = q.get('time_offset')
        return GroupCallStream(channel_id, scale, time_offset)
