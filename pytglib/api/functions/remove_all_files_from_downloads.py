

from ..utils import Object


class RemoveAllFilesFromDownloads(Object):
    """
    Removes all files from the file download list

    Attributes:
        ID (:obj:`str`): ``RemoveAllFilesFromDownloads``

    Args:
        only_active (:obj:`bool`):
            Pass true to remove only active downloads, including paused
        only_completed (:obj:`bool`):
            Pass true to remove only completed downloads
        delete_from_cache (:obj:`bool`):
            Pass true to delete the file from the TDLib file cache

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "removeAllFilesFromDownloads"

    def __init__(self, only_active, only_completed, delete_from_cache, extra=None, **kwargs):
        self.extra = extra
        self.only_active = only_active  # bool
        self.only_completed = only_completed  # bool
        self.delete_from_cache = delete_from_cache  # bool

    @staticmethod
    def read(q: dict, *args) -> "RemoveAllFilesFromDownloads":
        only_active = q.get('only_active')
        only_completed = q.get('only_completed')
        delete_from_cache = q.get('delete_from_cache')
        return RemoveAllFilesFromDownloads(only_active, only_completed, delete_from_cache)
