

from ..utils import Object


class FileTypeProfilePhoto(Object):
    """
    The file is a profile photo

    Attributes:
        ID (:obj:`str`): ``FileTypeProfilePhoto``

    No parameters required.

    Returns:
        FileType

    Raises:
        :class:`telegram.Error`
    """
    ID = "fileTypeProfilePhoto"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "FileTypeProfilePhoto":
        
        return FileTypeProfilePhoto()
