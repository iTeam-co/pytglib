

from ..utils import Object


class GetBlockedMessageSenders(Object):
    """
    Returns users and chats that were blocked by the current user 

    Attributes:
        ID (:obj:`str`): ``GetBlockedMessageSenders``

    Args:
        offset (:obj:`int`):
            Number of users and chats to skip in the result; must be non-negative 
        limit (:obj:`int`):
            The maximum number of users and chats to return; up to 100

    Returns:
        MessageSenders

    Raises:
        :class:`telegram.Error`
    """
    ID = "getBlockedMessageSenders"

    def __init__(self, offset, limit, extra=None, **kwargs):
        self.extra = extra
        self.offset = offset  # int
        self.limit = limit  # int

    @staticmethod
    def read(q: dict, *args) -> "GetBlockedMessageSenders":
        offset = q.get('offset')
        limit = q.get('limit')
        return GetBlockedMessageSenders(offset, limit)
