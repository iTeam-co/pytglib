

from ..utils import Object


class FileTypeVideoNote(Object):
    """
    The file is a video note

    Attributes:
        ID (:obj:`str`): ``FileTypeVideoNote``

    No parameters required.

    Returns:
        FileType

    Raises:
        :class:`telegram.Error`
    """
    ID = "fileTypeVideoNote"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "FileTypeVideoNote":
        
        return FileTypeVideoNote()
