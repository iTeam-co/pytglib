

from ..utils import Object


class DeviceTokenSimplePush(Object):
    """
    A token for Simple Push API for Firefox OS 

    Attributes:
        ID (:obj:`str`): ``DeviceTokenSimplePush``

    Args:
        endpoint (:obj:`str`):
            Absolute URL exposed by the push service where the application server can send push messages; may be empty to de-register a device

    Returns:
        DeviceToken

    Raises:
        :class:`telegram.Error`
    """
    ID = "deviceTokenSimplePush"

    def __init__(self, endpoint, **kwargs):
        
        self.endpoint = endpoint  # str

    @staticmethod
    def read(q: dict, *args) -> "DeviceTokenSimplePush":
        endpoint = q.get('endpoint')
        return DeviceTokenSimplePush(endpoint)
