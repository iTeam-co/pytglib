

from ..utils import Object


class UpdateFileRemovedFromDownloads(Object):
    """
    A file was removed from the file download list. This update is sent only after file download list is loaded for the first time 

    Attributes:
        ID (:obj:`str`): ``UpdateFileRemovedFromDownloads``

    Args:
        file_id (:obj:`int`):
            File identifier 
        counts (:class:`telegram.api.types.downloadedFileCounts`):
            New number of being downloaded and recently downloaded files found

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateFileRemovedFromDownloads"

    def __init__(self, file_id, counts, **kwargs):
        
        self.file_id = file_id  # int
        self.counts = counts  # DownloadedFileCounts

    @staticmethod
    def read(q: dict, *args) -> "UpdateFileRemovedFromDownloads":
        file_id = q.get('file_id')
        counts = Object.read(q.get('counts'))
        return UpdateFileRemovedFromDownloads(file_id, counts)
