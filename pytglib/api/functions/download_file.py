

from ..utils import Object


class DownloadFile(Object):
    """
    Asynchronously downloads a file from the cloud. updateFile will be used to notify about the download progress and successful completion of the download. Returns file state just after the download has been started

    Attributes:
        ID (:obj:`str`): ``DownloadFile``

    Args:
        file_id (:obj:`int`):
            Identifier of the file to download
        priority (:obj:`int`):
            Priority of the download (1-32)The higher the priority, the earlier the file will be downloadedIf the priorities of two files are equal, then the last one for which downloadFile was called will be downloaded first

    Returns:
        File

    Raises:
        :class:`telegram.Error`
    """
    ID = "downloadFile"

    def __init__(self, file_id, priority, extra=None, **kwargs):
        self.extra = extra
        self.file_id = file_id  # int
        self.priority = priority  # int

    @staticmethod
    def read(q: dict, *args) -> "DownloadFile":
        file_id = q.get('file_id')
        priority = q.get('priority')
        return DownloadFile(file_id, priority)
