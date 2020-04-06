

from ..utils import Object


class FileTypeWallpaper(Object):
    """
    The file is a wallpaper or a background pattern

    Attributes:
        ID (:obj:`str`): ``FileTypeWallpaper``

    No parameters required.

    Returns:
        FileType

    Raises:
        :class:`telegram.Error`
    """
    ID = "fileTypeWallpaper"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "FileTypeWallpaper":
        
        return FileTypeWallpaper()
