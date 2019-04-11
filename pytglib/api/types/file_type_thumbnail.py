

from ..utils import Object


class FileTypeThumbnail(Object):
    """
    The file is a thumbnail of another file

    Attributes:
        ID (:obj:`str`): ``FileTypeThumbnail``

    No parameters required.

    Returns:
        FileType

    Raises:
        :class:`telegram.Error`
    """
    ID = "fileTypeThumbnail"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "FileTypeThumbnail":
        
        return FileTypeThumbnail()
