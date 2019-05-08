

from ..utils import Object


class GetFileDownloadedPrefixSize(Object):
    """
    Returns file downloaded prefix size from a given offset 

    Attributes:
        ID (:obj:`str`): ``GetFileDownloadedPrefixSize``

    Args:
        file_id (:obj:`int`):
            Identifier of the file 
        offset (:obj:`int`):
            Offset from which downloaded prefix size should be calculated

    Returns:
        Count

    Raises:
        :class:`telegram.Error`
    """
    ID = "getFileDownloadedPrefixSize"

    def __init__(self, file_id, offset, extra=None, **kwargs):
        self.extra = extra
        self.file_id = file_id  # int
        self.offset = offset  # int

    @staticmethod
    def read(q: dict, *args) -> "GetFileDownloadedPrefixSize":
        file_id = q.get('file_id')
        offset = q.get('offset')
        return GetFileDownloadedPrefixSize(file_id, offset)
