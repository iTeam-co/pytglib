

from ..utils import Object


class OptimizeStorage(Object):
    """
    Optimizes storage usage, i.e. deletes some files and returns new storage usage statistics. Secret thumbnails can't be deleted

    Attributes:
        ID (:obj:`str`): ``OptimizeStorage``

    Args:
        size (:obj:`int`):
            Limit on the total size of files after deletionPass -1 to use the default limit
        ttl (:obj:`int`):
            Limit on the time that has passed since the last time a file was accessed (or creation time for some filesystems)Pass -1 to use the default limit
        count (:obj:`int`):
            Limit on the total count of files after deletionPass -1 to use the default limit
        immunity_delay (:obj:`int`):
            The amount of time after the creation of a file during which it can't be deleted, in secondsPass -1 to use the default value
        file_types (List of :class:`telegram.api.types.FileType`):
            If not empty, only files with the given type(s) are consideredBy default, all types except thumbnails, profile photos, stickers and wallpapers are deleted
        chat_ids (List of :obj:`int`):
            If not empty, only files from the given chats are consideredUse 0 as chat identifier to delete files not belonging to any chat (eg, profile photos)
        exclude_chat_ids (List of :obj:`int`):
            If not empty, files from the given chats are excludedUse 0 as chat identifier to exclude all files not belonging to any chat (eg, profile photos)
        return_deleted_file_statistics (:obj:`bool`):
            Pass true if deleted file statistics needs to be returned instead of the whole storage usage statisticsAffects only returned statistics
        chat_limit (:obj:`int`):
            Same as in getStorageStatisticsAffects only returned statistics

    Returns:
        StorageStatistics

    Raises:
        :class:`telegram.Error`
    """
    ID = "optimizeStorage"

    def __init__(self, size, ttl, count, immunity_delay, file_types, chat_ids, exclude_chat_ids, return_deleted_file_statistics, chat_limit, extra=None, **kwargs):
        self.extra = extra
        self.size = size  # int
        self.ttl = ttl  # int
        self.count = count  # int
        self.immunity_delay = immunity_delay  # int
        self.file_types = file_types  # list of FileType
        self.chat_ids = chat_ids  # list of int
        self.exclude_chat_ids = exclude_chat_ids  # list of int
        self.return_deleted_file_statistics = return_deleted_file_statistics  # bool
        self.chat_limit = chat_limit  # int

    @staticmethod
    def read(q: dict, *args) -> "OptimizeStorage":
        size = q.get('size')
        ttl = q.get('ttl')
        count = q.get('count')
        immunity_delay = q.get('immunity_delay')
        file_types = [Object.read(i) for i in q.get('file_types', [])]
        chat_ids = q.get('chat_ids')
        exclude_chat_ids = q.get('exclude_chat_ids')
        return_deleted_file_statistics = q.get('return_deleted_file_statistics')
        chat_limit = q.get('chat_limit')
        return OptimizeStorage(size, ttl, count, immunity_delay, file_types, chat_ids, exclude_chat_ids, return_deleted_file_statistics, chat_limit)
