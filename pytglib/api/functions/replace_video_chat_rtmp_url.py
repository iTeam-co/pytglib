

from ..utils import Object


class ReplaceVideoChatRtmpUrl(Object):
    """
    Replaces the current RTMP URL for streaming to the chat; requires creator privileges 

    Attributes:
        ID (:obj:`str`): ``ReplaceVideoChatRtmpUrl``

    Args:
        chat_id (:obj:`int`):
            Chat identifier

    Returns:
        RtmpUrl

    Raises:
        :class:`telegram.Error`
    """
    ID = "replaceVideoChatRtmpUrl"

    def __init__(self, chat_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int

    @staticmethod
    def read(q: dict, *args) -> "ReplaceVideoChatRtmpUrl":
        chat_id = q.get('chat_id')
        return ReplaceVideoChatRtmpUrl(chat_id)
