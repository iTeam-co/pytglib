

from ..utils import Object


class VideoNote(Object):
    """
    Describes a video note. The video must be equal in width and height, cropped to a circle, and stored in MPEG4 format 

    Attributes:
        ID (:obj:`str`): ``VideoNote``

    Args:
        duration (:obj:`int`):
            Duration of the video, in seconds; as defined by the sender 
        length (:obj:`int`):
            Video width and height; as defined by the sender 
        minithumbnail (:class:`telegram.api.types.minithumbnail`):
            Video minithumbnail; may be null 
        thumbnail (:class:`telegram.api.types.photoSize`):
            Video thumbnail; as defined by the sender; may be null 
        video (:class:`telegram.api.types.file`):
            File containing the video

    Returns:
        VideoNote

    Raises:
        :class:`telegram.Error`
    """
    ID = "videoNote"

    def __init__(self, duration, length, minithumbnail, thumbnail, video, **kwargs):
        
        self.duration = duration  # int
        self.length = length  # int
        self.minithumbnail = minithumbnail  # Minithumbnail
        self.thumbnail = thumbnail  # PhotoSize
        self.video = video  # File

    @staticmethod
    def read(q: dict, *args) -> "VideoNote":
        duration = q.get('duration')
        length = q.get('length')
        minithumbnail = Object.read(q.get('minithumbnail'))
        thumbnail = Object.read(q.get('thumbnail'))
        video = Object.read(q.get('video'))
        return VideoNote(duration, length, minithumbnail, thumbnail, video)
