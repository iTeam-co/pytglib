

from ..utils import Object


class UserStatusEmpty(Object):
    """
    The user status was never changed

    Attributes:
        ID (:obj:`str`): ``UserStatusEmpty``

    No parameters required.

    Returns:
        UserStatus

    Raises:
        :class:`telegram.Error`
    """
    ID = "userStatusEmpty"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "UserStatusEmpty":
        
        return UserStatusEmpty()
