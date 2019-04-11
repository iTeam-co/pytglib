

from ..utils import Object


class FileTypeSecret(Object):
    """
    The file was sent to a secret chat (the file type is not known to the server)

    Attributes:
        ID (:obj:`str`): ``FileTypeSecret``

    No parameters required.

    Returns:
        FileType

    Raises:
        :class:`telegram.Error`
    """
    ID = "fileTypeSecret"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "FileTypeSecret":
        
        return FileTypeSecret()
