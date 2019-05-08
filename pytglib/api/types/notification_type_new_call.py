

from ..utils import Object


class NotificationTypeNewCall(Object):
    """
    New call was received 

    Attributes:
        ID (:obj:`str`): ``NotificationTypeNewCall``

    Args:
        call_id (:obj:`int`):
            Call identifier

    Returns:
        NotificationType

    Raises:
        :class:`telegram.Error`
    """
    ID = "notificationTypeNewCall"

    def __init__(self, call_id, **kwargs):
        
        self.call_id = call_id  # int

    @staticmethod
    def read(q: dict, *args) -> "NotificationTypeNewCall":
        call_id = q.get('call_id')
        return NotificationTypeNewCall(call_id)
