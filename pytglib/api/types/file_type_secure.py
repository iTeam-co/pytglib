

from ..utils import Object


class FileTypeSecure(Object):
    """
    The file is a file from Secure storage used for storing Telegram Passport files

    Attributes:
        ID (:obj:`str`): ``FileTypeSecure``

    No parameters required.

    Returns:
        FileType

    Raises:
        :class:`telegram.Error`
    """
    ID = "fileTypeSecure"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "FileTypeSecure":
        
        return FileTypeSecure()
