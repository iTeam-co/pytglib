

from ..utils import Object


class UserStatusLastWeek(Object):
    """
    The user is offline, but was online last week

    Attributes:
        ID (:obj:`str`): ``UserStatusLastWeek``

    No parameters required.

    Returns:
        UserStatus

    Raises:
        :class:`telegram.Error`
    """
    ID = "userStatusLastWeek"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "UserStatusLastWeek":
        
        return UserStatusLastWeek()
