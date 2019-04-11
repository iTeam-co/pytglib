

from ..utils import Object


class Animation(Object):
    """
    Describes an animation file. The animation must be encoded in GIF or MPEG4 format 

    Attributes:
        ID (:obj:`str`): ``Animation``

    Args:
        duration (:obj:`int`):
            Duration of the animation, in seconds; as defined by the sender 
        width (:obj:`int`):
            Width of the animation 
        height (:obj:`int`):
            Height of the animation
        file_name (:obj:`str`):
            Original name of the file; as defined by the sender 
        mime_type (:obj:`str`):
            MIME type of the file, usually "image/gif" or "video/mp4" 
        thumbnail (:class:`telegram.api.types.photoSize`):
            Animation thumbnail; may be null 
        animation (:class:`telegram.api.types.file`):
            File containing the animation

    Returns:
        Animation

    Raises:
        :class:`telegram.Error`
    """
    ID = "animation"

    def __init__(self, duration, width, height, file_name, mime_type, thumbnail, animation, **kwargs):
        
        self.duration = duration  # int
        self.width = width  # int
        self.height = height  # int
        self.file_name = file_name  # str
        self.mime_type = mime_type  # str
        self.thumbnail = thumbnail  # PhotoSize
        self.animation = animation  # File

    @staticmethod
    def read(q: dict, *args) -> "Animation":
        duration = q.get('duration')
        width = q.get('width')
        height = q.get('height')
        file_name = q.get('file_name')
        mime_type = q.get('mime_type')
        thumbnail = Object.read(q.get('thumbnail'))
        animation = Object.read(q.get('animation'))
        return Animation(duration, width, height, file_name, mime_type, thumbnail, animation)
