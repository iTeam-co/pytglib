

from ..utils import Object


class FoundFileDownloads(Object):
    """
    Contains a list of downloaded files, found by a search

    Attributes:
        ID (:obj:`str`): ``FoundFileDownloads``

    Args:
        total_counts (:class:`telegram.api.types.downloadedFileCounts`):
            Total number of suitable files, ignoring offset
        files (List of :class:`telegram.api.types.fileDownload`):
            The list of files
        next_offset (:obj:`str`):
            The offset for the next requestIf empty, there are no more results

    Returns:
        FoundFileDownloads

    Raises:
        :class:`telegram.Error`
    """
    ID = "foundFileDownloads"

    def __init__(self, total_counts, files, next_offset, **kwargs):
        
        self.total_counts = total_counts  # DownloadedFileCounts
        self.files = files  # list of fileDownload
        self.next_offset = next_offset  # str

    @staticmethod
    def read(q: dict, *args) -> "FoundFileDownloads":
        total_counts = Object.read(q.get('total_counts'))
        files = [Object.read(i) for i in q.get('files', [])]
        next_offset = q.get('next_offset')
        return FoundFileDownloads(total_counts, files, next_offset)
