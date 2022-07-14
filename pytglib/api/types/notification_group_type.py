

from ..utils import Object


class NotificationGroupType(Object):
    """
    Describes the type of notifications in a notification group

    No parameters required.
    """
    ID = "notificationGroupType"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "NotificationGroupTypeMessages or NotificationGroupTypeCalls or NotificationGroupTypeSecretChat or NotificationGroupTypeMentions":
        if q.get("@type"):
            return Object.read(q)
        return NotificationGroupType()
