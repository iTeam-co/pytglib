

from ..utils import Object


class UpdateFileDownload(Object):
    """
    A file download was changed. This update is sent only after file download list is loaded for the first time 

    Attributes:
        ID (:obj:`str`): ``UpdateFileDownload``

    Args:
        file_id (:obj:`int`):
            File identifier
        complete_date (:obj:`int`):
            Point in time (Unix timestamp) when the file downloading was completed; 0 if the file downloading isn't completed
        is_paused (:obj:`bool`):
            True, if downloading of the file is paused
        counts (:class:`telegram.api.types.downloadedFileCounts`):
            New number of being downloaded and recently downloaded files found

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateFileDownload"

    def __init__(self, file_id, complete_date, is_paused, counts, **kwargs):
        
        self.file_id = file_id  # int
        self.complete_date = complete_date  # int
        self.is_paused = is_paused  # bool
        self.counts = counts  # DownloadedFileCounts

    @staticmethod
    def read(q: dict, *args) -> "UpdateFileDownload":
        file_id = q.get('file_id')
        complete_date = q.get('complete_date')
        is_paused = q.get('is_paused')
        counts = Object.read(q.get('counts'))
        return UpdateFileDownload(file_id, complete_date, is_paused, counts)
