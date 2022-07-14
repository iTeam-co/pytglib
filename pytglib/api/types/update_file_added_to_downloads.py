

from ..utils import Object


class UpdateFileAddedToDownloads(Object):
    """
    A file was added to the file download list. This update is sent only after file download list is loaded for the first time 

    Attributes:
        ID (:obj:`str`): ``UpdateFileAddedToDownloads``

    Args:
        file_download (:class:`telegram.api.types.fileDownload`):
            The added file download 
        counts (:class:`telegram.api.types.downloadedFileCounts`):
            New number of being downloaded and recently downloaded files found

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateFileAddedToDownloads"

    def __init__(self, file_download, counts, **kwargs):
        
        self.file_download = file_download  # FileDownload
        self.counts = counts  # DownloadedFileCounts

    @staticmethod
    def read(q: dict, *args) -> "UpdateFileAddedToDownloads":
        file_download = Object.read(q.get('file_download'))
        counts = Object.read(q.get('counts'))
        return UpdateFileAddedToDownloads(file_download, counts)
