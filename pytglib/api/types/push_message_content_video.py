

from ..utils import Object


class PushMessageContentVideo(Object):
    """
    A video message 

    Attributes:
        ID (:obj:`str`): ``PushMessageContentVideo``

    Args:
        video (:class:`telegram.api.types.video`):
            Message content; may be null 
        caption (:obj:`str`):
            Video caption 
        is_secret (:obj:`bool`):
            True, if the video is secret 
        is_pinned (:obj:`bool`):
            True, if the message is a pinned message with the specified content

    Returns:
        PushMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "pushMessageContentVideo"

    def __init__(self, video, caption, is_secret, is_pinned, **kwargs):
        
        self.video = video  # Video
        self.caption = caption  # str
        self.is_secret = is_secret  # bool
        self.is_pinned = is_pinned  # bool

    @staticmethod
    def read(q: dict, *args) -> "PushMessageContentVideo":
        video = Object.read(q.get('video'))
        caption = q.get('caption')
        is_secret = q.get('is_secret')
        is_pinned = q.get('is_pinned')
        return PushMessageContentVideo(video, caption, is_secret, is_pinned)
