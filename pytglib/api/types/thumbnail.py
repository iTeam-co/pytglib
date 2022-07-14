

from ..utils import Object


class Thumbnail(Object):
    """
    Represents a thumbnail 

    Attributes:
        ID (:obj:`str`): ``Thumbnail``

    Args:
        format (:class:`telegram.api.types.ThumbnailFormat`):
            Thumbnail format 
        width (:obj:`int`):
            Thumbnail width 
        height (:obj:`int`):
            Thumbnail height 
        file (:class:`telegram.api.types.file`):
            The thumbnail

    Returns:
        Thumbnail

    Raises:
        :class:`telegram.Error`
    """
    ID = "thumbnail"

    def __init__(self, format, width, height, file, **kwargs):
        
        self.format = format  # ThumbnailFormat
        self.width = width  # int
        self.height = height  # int
        self.file = file  # File

    @staticmethod
    def read(q: dict, *args) -> "Thumbnail":
        format = Object.read(q.get('format'))
        width = q.get('width')
        height = q.get('height')
        file = Object.read(q.get('file'))
        return Thumbnail(format, width, height, file)
