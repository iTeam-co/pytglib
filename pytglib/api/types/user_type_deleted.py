

from ..utils import Object


class UserTypeDeleted(Object):
    """
    A deleted user or deleted bot. No information on the user besides the user identifier is available. It is not possible to perform any active actions on this type of user

    Attributes:
        ID (:obj:`str`): ``UserTypeDeleted``

    No parameters required.

    Returns:
        UserType

    Raises:
        :class:`telegram.Error`
    """
    ID = "userTypeDeleted"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "UserTypeDeleted":
        
        return UserTypeDeleted()
