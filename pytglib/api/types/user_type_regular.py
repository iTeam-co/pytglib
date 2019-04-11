

from ..utils import Object


class UserTypeRegular(Object):
    """
    A regular user

    Attributes:
        ID (:obj:`str`): ``UserTypeRegular``

    No parameters required.

    Returns:
        UserType

    Raises:
        :class:`telegram.Error`
    """
    ID = "userTypeRegular"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "UserTypeRegular":
        
        return UserTypeRegular()
