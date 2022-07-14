

from ..utils import Object


class FileDownloadedPrefixSize(Object):
    """
    Contains size of downloaded prefix of a file 

    Attributes:
        ID (:obj:`str`): ``FileDownloadedPrefixSize``

    Args:
        size (:obj:`int`):
            The prefix size, in bytes

    Returns:
        FileDownloadedPrefixSize

    Raises:
        :class:`telegram.Error`
    """
    ID = "fileDownloadedPrefixSize"

    def __init__(self, size, **kwargs):
        
        self.size = size  # int

    @staticmethod
    def read(q: dict, *args) -> "FileDownloadedPrefixSize":
        size = q.get('size')
        return FileDownloadedPrefixSize(size)
