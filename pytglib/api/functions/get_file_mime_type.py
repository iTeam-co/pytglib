

from ..utils import Object


class GetFileMimeType(Object):
    """
    Returns the MIME type of a file, guessed by its extension. Returns an empty string on failure. This is an offline method. Can be called before authorization. Can be called synchronously 

    Attributes:
        ID (:obj:`str`): ``GetFileMimeType``

    Args:
        file_name (:obj:`str`):
            The name of the file or path to the file

    Returns:
        Text

    Raises:
        :class:`telegram.Error`
    """
    ID = "getFileMimeType"

    def __init__(self, file_name, extra=None, **kwargs):
        self.extra = extra
        self.file_name = file_name  # str

    @staticmethod
    def read(q: dict, *args) -> "GetFileMimeType":
        file_name = q.get('file_name')
        return GetFileMimeType(file_name)
