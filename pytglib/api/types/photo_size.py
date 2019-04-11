

from ..utils import Object


class PhotoSize(Object):
    """
    Photo description 

    Attributes:
        ID (:obj:`str`): ``PhotoSize``

    Args:
        type (:obj:`str`):
            Thumbnail type (see https://coretelegramorg/constructor/photoSize) 
        photo (:class:`telegram.api.types.file`):
            Information about the photo file 
        width (:obj:`int`):
            Photo width 
        height (:obj:`int`):
            Photo height

    Returns:
        PhotoSize

    Raises:
        :class:`telegram.Error`
    """
    ID = "photoSize"

    def __init__(self, type, photo, width, height, **kwargs):
        
        self.type = type  # str
        self.photo = photo  # File
        self.width = width  # int
        self.height = height  # int

    @staticmethod
    def read(q: dict, *args) -> "PhotoSize":
        type = q.get('type')
        photo = Object.read(q.get('photo'))
        width = q.get('width')
        height = q.get('height')
        return PhotoSize(type, photo, width, height)
