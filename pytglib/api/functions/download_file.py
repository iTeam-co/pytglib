

from ..utils import Object


class DownloadFile(Object):
    """
    Downloads a file from the cloud. Download progress and completion of the download will be notified through updateFile updates

    Attributes:
        ID (:obj:`str`): ``DownloadFile``

    Args:
        file_id (:obj:`int`):
            Identifier of the file to download
        priority (:obj:`int`):
            Priority of the download (1-32)The higher the priority, the earlier the file will be downloadedIf the priorities of two files are equal, then the last one for which downloadFile was called will be downloaded first
        offset (:obj:`int`):
            The starting position from which the file should be downloaded
        limit (:obj:`int`):
            Number of bytes which should be downloaded starting from the "offset" position before the download will be automatically cancelled; use 0 to download without a limit
        synchronous (:obj:`bool`):
            If false, this request returns file state just after the download has been startedIf true, this request returns file state only afterthe download has succeeded, has failed, has been cancelled or a new downloadFile request with different offset/limit parameters was sent

    Returns:
        File

    Raises:
        :class:`telegram.Error`
    """
    ID = "downloadFile"

    def __init__(self, file_id, priority, offset, limit, synchronous, extra=None, **kwargs):
        self.extra = extra
        self.file_id = file_id  # int
        self.priority = priority  # int
        self.offset = offset  # int
        self.limit = limit  # int
        self.synchronous = synchronous  # bool

    @staticmethod
    def read(q: dict, *args) -> "DownloadFile":
        file_id = q.get('file_id')
        priority = q.get('priority')
        offset = q.get('offset')
        limit = q.get('limit')
        synchronous = q.get('synchronous')
        return DownloadFile(file_id, priority, offset, limit, synchronous)
