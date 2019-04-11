

from ..utils import Object


class CleanFileName(Object):
    """
    Removes potentially dangerous characters from the name of a file. The encoding of the file name is supposed to be UTF-8. Returns an empty string on failure. This is an offline method. Can be called before authorization. Can be called synchronously 

    Attributes:
        ID (:obj:`str`): ``CleanFileName``

    Args:
        file_name (:obj:`str`):
            File name or path to the file

    Returns:
        Text

    Raises:
        :class:`telegram.Error`
    """
    ID = "cleanFileName"

    def __init__(self, file_name, extra=None, **kwargs):
        self.extra = extra
        self.file_name = file_name  # str

    @staticmethod
    def read(q: dict, *args) -> "CleanFileName":
        file_name = q.get('file_name')
        return CleanFileName(file_name)
