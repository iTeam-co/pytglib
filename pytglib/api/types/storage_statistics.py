

from ..utils import Object


class StorageStatistics(Object):
    """
    Contains the exact storage usage statistics split by chats and file type 

    Attributes:
        ID (:obj:`str`): ``StorageStatistics``

    Args:
        size (:obj:`int`):
            Total size of files 
        count (:obj:`int`):
            Total number of files 
        by_chat (List of :class:`telegram.api.types.storageStatisticsByChat`):
            Statistics split by chats

    Returns:
        StorageStatistics

    Raises:
        :class:`telegram.Error`
    """
    ID = "storageStatistics"

    def __init__(self, size, count, by_chat, **kwargs):
        
        self.size = size  # int
        self.count = count  # int
        self.by_chat = by_chat  # list of storageStatisticsByChat

    @staticmethod
    def read(q: dict, *args) -> "StorageStatistics":
        size = q.get('size')
        count = q.get('count')
        by_chat = [Object.read(i) for i in q.get('by_chat', [])]
        return StorageStatistics(size, count, by_chat)
