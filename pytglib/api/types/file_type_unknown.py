

from ..utils import Object


class FileTypeUnknown(Object):
    """
    The file type is not yet known

    Attributes:
        ID (:obj:`str`): ``FileTypeUnknown``

    No parameters required.

    Returns:
        FileType

    Raises:
        :class:`telegram.Error`
    """
    ID = "fileTypeUnknown"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "FileTypeUnknown":
        
        return FileTypeUnknown()
