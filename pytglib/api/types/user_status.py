

from ..utils import Object


class UserStatus(Object):
    """
    Describes the last time the user was online

    No parameters required.
    """
    ID = "userStatus"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "UserStatusLastWeek or UserStatusLastMonth or UserStatusOffline or UserStatusRecently or UserStatusOnline or UserStatusEmpty":
        if q.get("@type"):
            return Object.read(q)
        return UserStatus()
