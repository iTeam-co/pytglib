

from ..utils import Object


class InputMessageVideoNote(Object):
    """
    A video note message 

    Attributes:
        ID (:obj:`str`): ``InputMessageVideoNote``

    Args:
        video_note (:class:`telegram.api.types.InputFile`):
            Video note to be sent 
        thumbnail (:class:`telegram.api.types.inputThumbnail`):
            Video thumbnail, if available 
        duration (:obj:`int`):
            Duration of the video, in seconds 
        length (:obj:`int`):
            Video width and height; must be positive and not greater than 640

    Returns:
        InputMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputMessageVideoNote"

    def __init__(self, video_note, thumbnail, duration, length, **kwargs):
        
        self.video_note = video_note  # InputFile
        self.thumbnail = thumbnail  # InputThumbnail
        self.duration = duration  # int
        self.length = length  # int

    @staticmethod
    def read(q: dict, *args) -> "InputMessageVideoNote":
        video_note = Object.read(q.get('video_note'))
        thumbnail = Object.read(q.get('thumbnail'))
        duration = q.get('duration')
        length = q.get('length')
        return InputMessageVideoNote(video_note, thumbnail, duration, length)
