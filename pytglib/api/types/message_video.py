

from ..utils import Object


class MessageVideo(Object):
    """
    A video message 

    Attributes:
        ID (:obj:`str`): ``MessageVideo``

    Args:
        video (:class:`telegram.api.types.video`):
            The video description 
        caption (:class:`telegram.api.types.formattedText`):
            Video caption 
        is_secret (:obj:`bool`):
            True, if the video thumbnail must be blurred and the video must be shown only while tapped

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageVideo"

    def __init__(self, video, caption, is_secret, **kwargs):
        
        self.video = video  # Video
        self.caption = caption  # FormattedText
        self.is_secret = is_secret  # bool

    @staticmethod
    def read(q: dict, *args) -> "MessageVideo":
        video = Object.read(q.get('video'))
        caption = Object.read(q.get('caption'))
        is_secret = q.get('is_secret')
        return MessageVideo(video, caption, is_secret)
