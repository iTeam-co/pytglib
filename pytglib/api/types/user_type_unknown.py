

from ..utils import Object


class UserTypeUnknown(Object):
    """
    No information on the user besides the user identifier is available, yet this user has not been deleted. This object is extremely rare and must be handled like a deleted user. It is not possible to perform any actions on users of this type

    Attributes:
        ID (:obj:`str`): ``UserTypeUnknown``

    No parameters required.

    Returns:
        UserType

    Raises:
        :class:`telegram.Error`
    """
    ID = "userTypeUnknown"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "UserTypeUnknown":
        
        return UserTypeUnknown()
