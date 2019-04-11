

from ..utils import Object


class FileTypeSecretThumbnail(Object):
    """
    The file is a thumbnail of a file from a secret chat

    Attributes:
        ID (:obj:`str`): ``FileTypeSecretThumbnail``

    No parameters required.

    Returns:
        FileType

    Raises:
        :class:`telegram.Error`
    """
    ID = "fileTypeSecretThumbnail"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "FileTypeSecretThumbnail":
        
        return FileTypeSecretThumbnail()
