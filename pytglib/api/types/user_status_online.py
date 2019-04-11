

from ..utils import Object


class UserStatusOnline(Object):
    """
    The user is online 

    Attributes:
        ID (:obj:`str`): ``UserStatusOnline``

    Args:
        expires (:obj:`int`):
            Point in time (Unix timestamp) when the user's online status will expire

    Returns:
        UserStatus

    Raises:
        :class:`telegram.Error`
    """
    ID = "userStatusOnline"

    def __init__(self, expires, **kwargs):
        
        self.expires = expires  # int

    @staticmethod
    def read(q: dict, *args) -> "UserStatusOnline":
        expires = q.get('expires')
        return UserStatusOnline(expires)
