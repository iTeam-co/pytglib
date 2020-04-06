

from ..utils import Object


class Video(Object):
    """
    Describes a video file 

    Attributes:
        ID (:obj:`str`): ``Video``

    Args:
        duration (:obj:`int`):
            Duration of the video, in seconds; as defined by the sender 
        width (:obj:`int`):
            Video width; as defined by the sender 
        height (:obj:`int`):
            Video height; as defined by the sender
        file_name (:obj:`str`):
            Original name of the file; as defined by the sender 
        mime_type (:obj:`str`):
            MIME type of the file; as defined by the sender 
        has_stickers (:obj:`bool`):
            True, if stickers were added to the video
        supports_streaming (:obj:`bool`):
            True, if the video should be tried to be streamed 
        minithumbnail (:class:`telegram.api.types.minithumbnail`):
            Video minithumbnail; may be null 
        thumbnail (:class:`telegram.api.types.photoSize`):
            Video thumbnail; as defined by the sender; may be null 
        video (:class:`telegram.api.types.file`):
            File containing the video

    Returns:
        Video

    Raises:
        :class:`telegram.Error`
    """
    ID = "video"

    def __init__(self, duration, width, height, file_name, mime_type, has_stickers, supports_streaming, minithumbnail, thumbnail, video, **kwargs):
        
        self.duration = duration  # int
        self.width = width  # int
        self.height = height  # int
        self.file_name = file_name  # str
        self.mime_type = mime_type  # str
        self.has_stickers = has_stickers  # bool
        self.supports_streaming = supports_streaming  # bool
        self.minithumbnail = minithumbnail  # Minithumbnail
        self.thumbnail = thumbnail  # PhotoSize
        self.video = video  # File

    @staticmethod
    def read(q: dict, *args) -> "Video":
        duration = q.get('duration')
        width = q.get('width')
        height = q.get('height')
        file_name = q.get('file_name')
        mime_type = q.get('mime_type')
        has_stickers = q.get('has_stickers')
        supports_streaming = q.get('supports_streaming')
        minithumbnail = Object.read(q.get('minithumbnail'))
        thumbnail = Object.read(q.get('thumbnail'))
        video = Object.read(q.get('video'))
        return Video(duration, width, height, file_name, mime_type, has_stickers, supports_streaming, minithumbnail, thumbnail, video)
