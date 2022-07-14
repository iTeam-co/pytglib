

from ..utils import Object


class TextEntityTypeMediaTimestamp(Object):
    """
    A media timestamp 

    Attributes:
        ID (:obj:`str`): ``TextEntityTypeMediaTimestamp``

    Args:
        media_timestamp (:obj:`int`):
            Timestamp from which a video/audio/video note/voice note playing must start, in secondsThe media can be in the content or the web page preview of the current message, or in the same places in the replied message

    Returns:
        TextEntityType

    Raises:
        :class:`telegram.Error`
    """
    ID = "textEntityTypeMediaTimestamp"

    def __init__(self, media_timestamp, **kwargs):
        
        self.media_timestamp = media_timestamp  # int

    @staticmethod
    def read(q: dict, *args) -> "TextEntityTypeMediaTimestamp":
        media_timestamp = q.get('media_timestamp')
        return TextEntityTypeMediaTimestamp(media_timestamp)
