

from ..utils import Object


class PushMessageContentVideoNote(Object):
    """
    A video note message 

    Attributes:
        ID (:obj:`str`): ``PushMessageContentVideoNote``

    Args:
        video_note (:class:`telegram.api.types.videoNote`):
            Message content; may be null 
        is_pinned (:obj:`bool`):
            True, if the message is a pinned message with the specified content

    Returns:
        PushMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "pushMessageContentVideoNote"

    def __init__(self, video_note, is_pinned, **kwargs):
        
        self.video_note = video_note  # VideoNote
        self.is_pinned = is_pinned  # bool

    @staticmethod
    def read(q: dict, *args) -> "PushMessageContentVideoNote":
        video_note = Object.read(q.get('video_note'))
        is_pinned = q.get('is_pinned')
        return PushMessageContentVideoNote(video_note, is_pinned)
