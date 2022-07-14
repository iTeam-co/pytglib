

from ..utils import Object


class DownloadedFileCounts(Object):
    """
    Contains number of being downloaded and recently downloaded files found

    Attributes:
        ID (:obj:`str`): ``DownloadedFileCounts``

    Args:
        active_count (:obj:`int`):
            Number of active file downloads found, including paused
        paused_count (:obj:`int`):
            Number of paused file downloads found
        completed_count (:obj:`int`):
            Number of completed file downloads found

    Returns:
        DownloadedFileCounts

    Raises:
        :class:`telegram.Error`
    """
    ID = "downloadedFileCounts"

    def __init__(self, active_count, paused_count, completed_count, **kwargs):
        
        self.active_count = active_count  # int
        self.paused_count = paused_count  # int
        self.completed_count = completed_count  # int

    @staticmethod
    def read(q: dict, *args) -> "DownloadedFileCounts":
        active_count = q.get('active_count')
        paused_count = q.get('paused_count')
        completed_count = q.get('completed_count')
        return DownloadedFileCounts(active_count, paused_count, completed_count)
