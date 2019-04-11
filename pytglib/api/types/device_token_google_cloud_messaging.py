

from ..utils import Object


class DeviceTokenGoogleCloudMessaging(Object):
    """
    A token for Google Cloud Messaging 

    Attributes:
        ID (:obj:`str`): ``DeviceTokenGoogleCloudMessaging``

    Args:
        token (:obj:`str`):
            Device registration token; may be empty to de-register a device

    Returns:
        DeviceToken

    Raises:
        :class:`telegram.Error`
    """
    ID = "deviceTokenGoogleCloudMessaging"

    def __init__(self, token, **kwargs):
        
        self.token = token  # str

    @staticmethod
    def read(q: dict, *args) -> "DeviceTokenGoogleCloudMessaging":
        token = q.get('token')
        return DeviceTokenGoogleCloudMessaging(token)
