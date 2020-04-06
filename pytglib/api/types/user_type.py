

from ..utils import Object


class UserType(Object):
    """
    Represents the type of a user. The following types are possible: regular users, deleted users and bots

    No parameters required.
    """
    ID = "userType"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "UserTypeBot or UserTypeDeleted or UserTypeUnknown or UserTypeRegular":
        if q.get("@type"):
            return Object.read(q)
        return UserType()
