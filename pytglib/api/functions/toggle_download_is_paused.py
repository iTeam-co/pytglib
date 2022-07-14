

from ..utils import Object


class ToggleDownloadIsPaused(Object):
    """
    Changes pause state of a file in the file download list

    Attributes:
        ID (:obj:`str`): ``ToggleDownloadIsPaused``

    Args:
        file_id (:obj:`int`):
            Identifier of the downloaded file
        is_paused (:obj:`bool`):
            Pass true if the download is paused

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "toggleDownloadIsPaused"

    def __init__(self, file_id, is_paused, extra=None, **kwargs):
        self.extra = extra
        self.file_id = file_id  # int
        self.is_paused = is_paused  # bool

    @staticmethod
    def read(q: dict, *args) -> "ToggleDownloadIsPaused":
        file_id = q.get('file_id')
        is_paused = q.get('is_paused')
        return ToggleDownloadIsPaused(file_id, is_paused)
