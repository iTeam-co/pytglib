

from ..utils import Object


class FileTypePhoto(Object):
    """
    The file is a photo

    Attributes:
        ID (:obj:`str`): ``FileTypePhoto``

    No parameters required.

    Returns:
        FileType

    Raises:
        :class:`telegram.Error`
    """
    ID = "fileTypePhoto"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "FileTypePhoto":
        
        return FileTypePhoto()
