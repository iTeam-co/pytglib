

from ..utils import Object


class GetStorageStatistics(Object):
    """
    Returns storage usage statistics. Can be called before authorization 

    Attributes:
        ID (:obj:`str`): ``GetStorageStatistics``

    Args:
        chat_limit (:obj:`int`):
            The maximum number of chats with the largest storage usage for which separate statistics should be returnedAll other chats will be grouped in entries with chat_id == 0If the chat info database is not used, the chat_limit is ignored and is always set to 0

    Returns:
        StorageStatistics

    Raises:
        :class:`telegram.Error`
    """
    ID = "getStorageStatistics"

    def __init__(self, chat_limit, extra=None, **kwargs):
        self.extra = extra
        self.chat_limit = chat_limit  # int

    @staticmethod
    def read(q: dict, *args) -> "GetStorageStatistics":
        chat_limit = q.get('chat_limit')
        return GetStorageStatistics(chat_limit)
