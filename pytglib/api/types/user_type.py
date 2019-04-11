

from ..utils import Object


class UserType(Object):
    """
    Represents the type of the user. The following types are possible: regular users, deleted users and bots

    No parameters required.
    """
    ID = "userType"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "UserTypeRegular or UserTypeBot or UserTypeDeleted or UserTypeUnknown":
        if q.get("@type"):
            return Object.read(q)
        return UserType()
