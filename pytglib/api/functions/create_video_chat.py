

from ..utils import Object


class CreateVideoChat(Object):
    """
    Creates a video chat (a group call bound to a chat). Available only for basic groups, supergroups and channels; requires can_manage_video_chats rights

    Attributes:
        ID (:obj:`str`): ``CreateVideoChat``

    Args:
        chat_id (:obj:`int`):
            Identifier of a chat in which the video chat will be created
        title (:obj:`str`):
            Group call title; if empty, chat title will be used
        start_date (:obj:`int`):
            Point in time (Unix timestamp) when the group call is supposed to be started by an administrator; 0 to start the video chat immediatelyThe date must be at least 10 seconds and at most 8 days in the future
        is_rtmp_stream (:obj:`bool`):
            Pass true to create an RTMP stream instead of an ordinary video chat; requires creator privileges

    Returns:
        GroupCallId

    Raises:
        :class:`telegram.Error`
    """
    ID = "createVideoChat"

    def __init__(self, chat_id, title, start_date, is_rtmp_stream, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.title = title  # str
        self.start_date = start_date  # int
        self.is_rtmp_stream = is_rtmp_stream  # bool

    @staticmethod
    def read(q: dict, *args) -> "CreateVideoChat":
        chat_id = q.get('chat_id')
        title = q.get('title')
        start_date = q.get('start_date')
        is_rtmp_stream = q.get('is_rtmp_stream')
        return CreateVideoChat(chat_id, title, start_date, is_rtmp_stream)
