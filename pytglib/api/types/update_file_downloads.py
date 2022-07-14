

from ..utils import Object


class UpdateFileDownloads(Object):
    """
    The state of the file download list has changed

    Attributes:
        ID (:obj:`str`): ``UpdateFileDownloads``

    Args:
        total_size (:obj:`int`):
            Total size of files in the file download list, in bytes
        total_count (:obj:`int`):
            Total number of files in the file download list
        downloaded_size (:obj:`int`):
            Total downloaded size of files in the file download list, in bytes

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateFileDownloads"

    def __init__(self, total_size, total_count, downloaded_size, **kwargs):
        
        self.total_size = total_size  # int
        self.total_count = total_count  # int
        self.downloaded_size = downloaded_size  # int

    @staticmethod
    def read(q: dict, *args) -> "UpdateFileDownloads":
        total_size = q.get('total_size')
        total_count = q.get('total_count')
        downloaded_size = q.get('downloaded_size')
        return UpdateFileDownloads(total_size, total_count, downloaded_size)
