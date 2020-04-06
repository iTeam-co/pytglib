

from ..utils import Object


class GetBlockedUsers(Object):
    """
    Returns users that were blocked by the current user 

    Attributes:
        ID (:obj:`str`): ``GetBlockedUsers``

    Args:
        offset (:obj:`int`):
            Number of users to skip in the result; must be non-negative 
        limit (:obj:`int`):
            The maximum number of users to return; up to 100

    Returns:
        Users

    Raises:
        :class:`telegram.Error`
    """
    ID = "getBlockedUsers"

    def __init__(self, offset, limit, extra=None, **kwargs):
        self.extra = extra
        self.offset = offset  # int
        self.limit = limit  # int

    @staticmethod
    def read(q: dict, *args) -> "GetBlockedUsers":
        offset = q.get('offset')
        limit = q.get('limit')
        return GetBlockedUsers(offset, limit)
