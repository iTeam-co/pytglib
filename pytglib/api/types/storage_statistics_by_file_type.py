

from ..utils import Object


class StorageStatisticsByFileType(Object):
    """
    Contains the storage usage statistics for a specific file type 

    Attributes:
        ID (:obj:`str`): ``StorageStatisticsByFileType``

    Args:
        file_type (:class:`telegram.api.types.FileType`):
            File type 
        size (:obj:`int`):
            Total size of the files 
        count (:obj:`int`):
            Total number of files

    Returns:
        StorageStatisticsByFileType

    Raises:
        :class:`telegram.Error`
    """
    ID = "storageStatisticsByFileType"

    def __init__(self, file_type, size, count, **kwargs):
        
        self.file_type = file_type  # FileType
        self.size = size  # int
        self.count = count  # int

    @staticmethod
    def read(q: dict, *args) -> "StorageStatisticsByFileType":
        file_type = Object.read(q.get('file_type'))
        size = q.get('size')
        count = q.get('count')
        return StorageStatisticsByFileType(file_type, size, count)
