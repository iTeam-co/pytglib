

from ..utils import Object


class NotificationGroupTypeCalls(Object):
    """
    A group containing notifications of type notificationTypeNewCall

    Attributes:
        ID (:obj:`str`): ``NotificationGroupTypeCalls``

    No parameters required.

    Returns:
        NotificationGroupType

    Raises:
        :class:`telegram.Error`
    """
    ID = "notificationGroupTypeCalls"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "NotificationGroupTypeCalls":
        
        return NotificationGroupTypeCalls()
