

from ..utils import Object


class GetUser(Object):
    """
    Returns information about a user by their identifier. This is an offline request if the current user is not a bot 

    Attributes:
        ID (:obj:`str`): ``GetUser``

    Args:
        user_id (:obj:`int`):
            User identifier

    Returns:
        User

    Raises:
        :class:`telegram.Error`
    """
    ID = "getUser"

    def __init__(self, user_id, extra=None, **kwargs):
        self.extra = extra
        self.user_id = user_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetUser":
        user_id = q.get('user_id')
        return GetUser(user_id)
