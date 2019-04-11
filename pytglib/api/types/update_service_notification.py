

from ..utils import Object


class UpdateServiceNotification(Object):
    """
    Service notification from the server. Upon receiving this the client must show a popup with the content of the notification

    Attributes:
        ID (:obj:`str`): ``UpdateServiceNotification``

    Args:
        type (:obj:`str`):
            Notification typeIf type begins with "AUTH_KEY_DROP_", then two buttons "Cancel" and "Log out" should be shown under notification; if user presses the second, all local data should be destroyed using Destroy method
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
