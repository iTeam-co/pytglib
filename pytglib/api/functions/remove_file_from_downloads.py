

from ..utils import Object


class RemoveFileFromDownloads(Object):
    """
    Removes a file from the file download list 

    Attributes:
        ID (:obj:`str`): ``RemoveFileFromDownloads``

    Args:
        file_id (:obj:`int`):
            Identifier of the downloaded file 
        delete_from_cache (:obj:`bool`):
            Pass true to delete the file from the TDLib file cache

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "removeFileFromDownloads"

    def __init__(self, file_id, delete_from_cache, extra=None, **kwargs):
        self.extra = extra
        self.file_id = file_id  # int
        self.delete_from_cache = delete_from_cache  # bool

    @staticmethod
    def read(q: dict, *args) -> "RemoveFileFromDownloads":
        file_id = q.get('file_id')
        delete_from_cache = q.get('delete_from_cache')
        return RemoveFileFromDownloads(file_id, delete_from_cache)
