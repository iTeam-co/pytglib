

from ..utils import Object


class UserStatusOffline(Object):
    """
    The user is offline 

    Attributes:
        ID (:obj:`str`): ``UserStatusOffline``

    Args:
        was_online (:obj:`int`):
            Point in time (Unix timestamp) when the user was last online

    Returns:
        UserStatus

    Raises:
        :class:`telegram.Error`
    """
    ID = "userStatusOffline"

    def __init__(self, was_online, **kwargs):
        
        self.was_online = was_online  # int

    @staticmethod
    def read(q: dict, *args) -> "UserStatusOffline":
        was_online = q.get('was_online')
        return UserStatusOffline(was_online)
