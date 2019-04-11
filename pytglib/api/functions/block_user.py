

from ..utils import Object


class BlockUser(Object):
    """
    Adds a user to the blacklist 

    Attributes:
        ID (:obj:`str`): ``BlockUser``

    Args:
        user_id (:obj:`int`):
            User identifier

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "blockUser"

    def __init__(self, user_id, extra=None, **kwargs):
        self.extra = extra
        self.user_id = user_id  # int

    @staticmethod
    def read(q: dict, *args) -> "BlockUser":
        user_id = q.get('user_id')
        return BlockUser(user_id)
