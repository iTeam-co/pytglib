

from ..utils import Object


class StorageStatisticsFast(Object):
    """
    Contains approximate storage usage statistics, excluding files of unknown file type 

    Attributes:
        ID (:obj:`str`): ``StorageStatisticsFast``

    Args:
        files_size (:obj:`int`):
            Approximate total size of files 
        file_count (:obj:`int`):
            Approximate number of files 
        database_size (:obj:`int`):
            Size of the database

    Returns:
        StorageStatisticsFast

    Raises:
        :class:`telegram.Error`
    """
    ID = "storageStatisticsFast"

    def __init__(self, files_size, file_count, database_size, **kwargs):
        
        self.files_size = files_size  # int
        self.file_count = file_count  # int
        self.database_size = database_size  # int

    @staticmethod
    def read(q: dict, *args) -> "StorageStatisticsFast":
        files_size = q.get('files_size')
        file_count = q.get('file_count')
        database_size = q.get('database_size')
        return StorageStatisticsFast(files_size, file_count, database_size)
