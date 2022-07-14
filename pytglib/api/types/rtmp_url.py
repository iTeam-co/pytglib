

from ..utils import Object


class RtmpUrl(Object):
    """
    Represents an RTMP url 

    Attributes:
        ID (:obj:`str`): ``RtmpUrl``

    Args:
        url (:obj:`str`):
            The URL 
        stream_key (:obj:`str`):
            Stream key

    Returns:
        RtmpUrl

    Raises:
        :class:`telegram.Error`
    """
    ID = "rtmpUrl"

    def __init__(self, url, stream_key, **kwargs):
        
        self.url = url  # str
        self.stream_key = stream_key  # str

    @staticmethod
    def read(q: dict, *args) -> "RtmpUrl":
        url = q.get('url')
        stream_key = q.get('stream_key')
        return RtmpUrl(url, stream_key)
