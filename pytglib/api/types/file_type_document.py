

from ..utils import Object


class FileTypeDocument(Object):
    """
    The file is a document

    Attributes:
        ID (:obj:`str`): ``FileTypeDocument``

    No parameters required.

    Returns:
        FileType

    Raises:
        :class:`telegram.Error`
    """
    ID = "fileTypeDocument"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "FileTypeDocument":
        
        return FileTypeDocument()
