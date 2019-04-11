

from ..utils import Object


class StorageStatisticsByChat(Object):
    """
    Contains the storage usage statistics for a specific chat 

    Attributes:
        ID (:obj:`str`): ``StorageStatisticsByChat``

    Args:
        chat_id (:obj:`int`):
            Chat identifier; 0 if none 
        size (:obj:`int`):
            Total size of the files in the chat 
        count (:obj:`int`):
            Total number of files in the chat 
        by_file_type (List of :class:`telegram.api.types.storageStatisticsByFileType`):
            Statistics split by file types

    Returns:
        StorageStatisticsByChat

    Raises:
        :class:`telegram.Error`
    """
    ID = "storageStatisticsByChat"

    def __init__(self, chat_id, size, count, by_file_type, **kwargs):
        
        self.chat_id = chat_id  # int
        self.size = size  # int
        self.count = count  # int
        self.by_file_type = by_file_type  # list of storageStatisticsByFileType

    @staticmethod
    def read(q: dict, *args) -> "StorageStatisticsByChat":
        chat_id = q.get('chat_id')
        size = q.get('size')
        count = q.get('count')
        by_file_type = [Object.read(i) for i in q.get('by_file_type', [])]
        return StorageStatisticsByChat(chat_id, size, count, by_file_type)
