

from ..utils import Object


class MessageVideoNote(Object):
    """
    A video note message 

    Attributes:
        ID (:obj:`str`): ``MessageVideoNote``

    Args:
        video_note (:class:`telegram.api.types.videoNote`):
            The video note description 
        is_viewed (:obj:`bool`):
            True, if at least one of the recipients has viewed the video note 
        is_secret (:obj:`bool`):
            True, if the video note thumbnail must be blurred and the video note must be shown only while tapped

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageVideoNote"

    def __init__(self, video_note, is_viewed, is_secret, **kwargs):
        
        self.video_note = video_note  # VideoNote
        self.is_viewed = is_viewed  # bool
        self.is_secret = is_secret  # bool

    @staticmethod
    def read(q: dict, *args) -> "MessageVideoNote":
        video_note = Object.read(q.get('video_note'))
        is_viewed = q.get('is_viewed')
        is_secret = q.get('is_secret')
        return MessageVideoNote(video_note, is_viewed, is_secret)
