

from ..utils import Object


class FileTypeNone(Object):
    """
    The data is not a file

    Attributes:
        ID (:obj:`str`): ``FileTypeNone``

    No parameters required.

    Returns:
        FileType

    Raises:
        :class:`telegram.Error`
    """
    ID = "fileTypeNone"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "FileTypeNone":
        
        return FileTypeNone()
