

from ..utils import Object


class PhotoSize(Object):
    """
    Describes an image in JPEG format 

    Attributes:
        ID (:obj:`str`): ``PhotoSize``

    Args:
        type (:obj:`str`):
            Image type (see https://coretelegramorg/constructor/photoSize)
        photo (:class:`telegram.api.types.file`):
            Information about the image file 
        width (:obj:`int`):
            Image width 
        height (:obj:`int`):
            Image height
        progressive_sizes (List of :obj:`int`):
            Sizes of progressive JPEG file prefixes, which can be used to preliminarily show the image; in bytes

    Returns:
        PhotoSize

    Raises:
        :class:`telegram.Error`
    """
    ID = "photoSize"

    def __init__(self, type, photo, width, height, progressive_sizes, **kwargs):
        
        self.type = type  # str
        self.photo = photo  # File
        self.width = width  # int
        self.height = height  # int
        self.progressive_sizes = progressive_sizes  # list of int

    @staticmethod
    def read(q: dict, *args) -> "PhotoSize":
        type = q.get('type')
        photo = Object.read(q.get('photo'))
        width = q.get('width')
        height = q.get('height')
        progressive_sizes = q.get('progressive_sizes')
        return PhotoSize(type, photo, width, height, progressive_sizes)
