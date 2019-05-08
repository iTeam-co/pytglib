

from ..utils import Object


class ProcessPushNotification(Object):
    """
    Handles a push notification. Returns error with code 406 if the push notification is not supported and connection to the server is required to fetch new data. Can be called before authorization

    Attributes:
        ID (:obj:`str`): ``ProcessPushNotification``

    Args:
        payload (:obj:`str`):
            JSON-encoded push notification payload with all fields sent by the server, and "googlesent_time" and "googlenotificationsound" fields added

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "processPushNotification"

    def __init__(self, payload, extra=None, **kwargs):
        self.extra = extra
        self.payload = payload  # str

    @staticmethod
    def read(q: dict, *args) -> "ProcessPushNotification":
        payload = q.get('payload')
        return ProcessPushNotification(payload)
