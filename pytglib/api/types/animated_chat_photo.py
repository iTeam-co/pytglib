

from ..utils import Object


class AnimatedChatPhoto(Object):
    """
    Animated variant of a chat photo in MPEG4 format

    Attributes:
        ID (:obj:`str`): ``AnimatedChatPhoto``

    Args:
        length (:obj:`int`):
            Animation width and height
        file (:class:`telegram.api.types.file`):
            Information about the animation file
        main_frame_timestamp (:obj:`float`):
            Timestamp of the frame, used as a static chat photo

    Returns:
        AnimatedChatPhoto

    Raises:
        :class:`telegram.Error`
    """
    ID = "animatedChatPhoto"

    def __init__(self, length, file, main_frame_timestamp, **kwargs):
        
        self.length = length  # int
        self.file = file  # File
        self.main_frame_timestamp = main_frame_timestamp  # float

    @staticmethod
    def read(q: dict, *args) -> "AnimatedChatPhoto":
        length = q.get('length')
        file = Object.read(q.get('file'))
        main_frame_timestamp = q.get('main_frame_timestamp')
        return AnimatedChatPhoto(length, file, main_frame_timestamp)
