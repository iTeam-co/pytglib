

from ..utils import Object


class GetFileExtension(Object):
    """
    Returns the extension of a file, guessed by its MIME type. Returns an empty string on failure. This is an offline method. Can be called before authorization. Can be called synchronously 

    Attributes:
        ID (:obj:`str`): ``GetFileExtension``

    Args:
        mime_type (:obj:`str`):
            The MIME type of the file

    Returns:
        Text

    Raises:
        :class:`telegram.Error`
    """
    ID = "getFileExtension"

    def __init__(self, mime_type, extra=None, **kwargs):
        self.extra = extra
        self.mime_type = mime_type  # str

    @staticmethod
    def read(q: dict, *args) -> "GetFileExtension":
        mime_type = q.get('mime_type')
        return GetFileExtension(mime_type)
