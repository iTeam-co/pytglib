

from ..utils import Object


class UserStatusLastMonth(Object):
    """
    The user is offline, but was online last month

    Attributes:
        ID (:obj:`str`): ``UserStatusLastMonth``

    No parameters required.

    Returns:
        UserStatus

    Raises:
        :class:`telegram.Error`
    """
    ID = "userStatusLastMonth"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "UserStatusLastMonth":
        
        return UserStatusLastMonth()
