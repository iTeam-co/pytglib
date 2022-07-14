

from ..utils import Object


class UpdateServiceNotification(Object):
    """
    A service notification from the server was received. Upon receiving this the application must show a popup with the content of the notification

    Attributes:
        ID (:obj:`str`): ``UpdateServiceNotification``

    Args:
        type (:obj:`str`):
            Notification typeIf type begins with "AUTH_KEY_DROP_", then two buttons "Cancel" and "Log out" must be shown under notification; if user presses the second, all local data must be destroyed using Destroy method
        content (:class:`telegram.api.types.MessageContent`):
            Notification content

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateServiceNotification"

    def __init__(self, type, content, **kwargs):
        
        self.type = type  # str
        self.content = content  # MessageContent

    @staticmethod
    def read(q: dict, *args) -> "UpdateServiceNotification":
        type = q.get('type')
        content = Object.read(q.get('content'))
        return UpdateServiceNotification(type, content)
