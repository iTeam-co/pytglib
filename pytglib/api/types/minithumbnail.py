

from ..utils import Object


class Minithumbnail(Object):
    """
    Thumbnail image of a very poor quality and low resolution 

    Attributes:
        ID (:obj:`str`): ``Minithumbnail``

    Args:
        width (:obj:`int`):
            Thumbnail width, usually doesn't exceed 40 
        height (:obj:`int`):
            Thumbnail height, usually doesn't exceed 40 
        data (:obj:`bytes`):
            The thumbnail in JPEG format

    Returns:
        Minithumbnail

    Raises:
        :class:`telegram.Error`
    """
    ID = "minithumbnail"

    def __init__(self, width, height, data, **kwargs):
        
        self.width = width  # int
        self.height = height  # int
        self.data = data  # bytes

    @staticmethod
    def read(q: dict, *args) -> "Minithumbnail":
        width = q.get('width')
        height = q.get('height')
        data = q.get('data')
        return Minithumbnail(width, height, data)
