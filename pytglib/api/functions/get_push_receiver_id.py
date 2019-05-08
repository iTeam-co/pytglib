

from ..utils import Object


class GetPushReceiverId(Object):
    """
    Returns a globally unique push notification subscription identifier for identification of an account, which has received a push notification. This is an offline method. Can be called before authorization. Can be called synchronously 

    Attributes:
        ID (:obj:`str`): ``GetPushReceiverId``

    Args:
        payload (:obj:`str`):
            JSON-encoded push notification payload

    Returns:
        PushReceiverId

    Raises:
        :class:`telegram.Error`
    """
    ID = "getPushReceiverId"

    def __init__(self, payload, extra=None, **kwargs):
        self.extra = extra
        self.payload = payload  # str

    @staticmethod
    def read(q: dict, *args) -> "GetPushReceiverId":
        payload = q.get('payload')
        return GetPushReceiverId(payload)
