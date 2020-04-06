

from ..utils import Object


class InputThumbnail(Object):
    """
    A thumbnail to be sent along with a file; should be in JPEG or WEBP format for stickers, and less than 200 KB in size 

    Attributes:
        ID (:obj:`str`): ``InputThumbnail``

    Args:
        thumbnail (:class:`telegram.api.types.InputFile`):
            Thumbnail file to sendSending thumbnails by file_id is currently not supported
        width (:obj:`int`):
            Thumbnail width, usually shouldn't exceed 320Use 0 if unknown 
        height (:obj:`int`):
            Thumbnail height, usually shouldn't exceed 320Use 0 if unknown

    Returns:
        InputThumbnail

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputThumbnail"

    def __init__(self, thumbnail, width, height, **kwargs):
        
        self.thumbnail = thumbnail  # InputFile
        self.width = width  # int
        self.height = height  # int

    @staticmethod
    def read(q: dict, *args) -> "InputThumbnail":
        thumbnail = Object.read(q.get('thumbnail'))
        width = q.get('width')
        height = q.get('height')
        return InputThumbnail(thumbnail, width, height)
