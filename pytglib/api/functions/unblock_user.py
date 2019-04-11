

from ..utils import Object


class UnblockUser(Object):
    """
    Removes a user from the blacklist 

    Attributes:
        ID (:obj:`str`): ``UnblockUser``

    Args:
        user_id (:obj:`int`):
            User identifier

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "unblockUser"

    def __init__(self, user_id, extra=None, **kwargs):
        self.extra = extra
        self.user_id = user_id  # int

    @staticmethod
    def read(q: dict, *args) -> "UnblockUser":
        user_id = q.get('user_id')
        return UnblockUser(user_id)
