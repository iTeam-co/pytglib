

from ..utils import Object


class GetVideoChatRtmpUrl(Object):
    """
    Returns RTMP URL for streaming to the chat; requires creator privileges 

    Attributes:
        ID (:obj:`str`): ``GetVideoChatRtmpUrl``

    Args:
        chat_id (:obj:`int`):
            Chat identifier

    Returns:
        RtmpUrl

    Raises:
        :class:`telegram.Error`
    """
    ID = "getVideoChatRtmpUrl"

    def __init__(self, chat_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetVideoChatRtmpUrl":
        chat_id = q.get('chat_id')
        return GetVideoChatRtmpUrl(chat_id)
