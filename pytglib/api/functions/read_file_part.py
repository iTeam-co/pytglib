

from ..utils import Object


class ReadFilePart(Object):
    """
    Reads a part of a file from the TDLib file cache and returns read bytes. This method is intended to be used only if the client has no direct access to TDLib's file system, because it is usually slower than a direct read from the file

    Attributes:
        ID (:obj:`str`): ``ReadFilePart``

    Args:
        file_id (:obj:`int`):
            Identifier of the fileThe file must be located in the TDLib file cache
        offset (:obj:`int`):
            The offset from which to read the file
        count (:obj:`int`):
            Number of bytes to readAn error will be returned if there are not enough bytes available in the file from the specified positionPass 0 to read all available data from the specified position

    Returns:
        FilePart

    Raises:
        :class:`telegram.Error`
    """
    ID = "readFilePart"

    def __init__(self, file_id, offset, count, extra=None, **kwargs):
        self.extra = extra
        self.file_id = file_id  # int
        self.offset = offset  # int
        self.count = count  # int

    @staticmethod
    def read(q: dict, *args) -> "ReadFilePart":
        file_id = q.get('file_id')
        offset = q.get('offset')
        count = q.get('count')
        return ReadFilePart(file_id, offset, count)
