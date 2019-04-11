

from ..utils import Object


class UserStatusRecently(Object):
    """
    The user was online recently

    Attributes:
        ID (:obj:`str`): ``UserStatusRecently``

    No parameters required.

    Returns:
        UserStatus

    Raises:
        :class:`telegram.Error`
    """
    ID = "userStatusRecently"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "UserStatusRecently":
        
        return UserStatusRecently()
