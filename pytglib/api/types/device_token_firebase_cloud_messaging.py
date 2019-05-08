

from ..utils import Object


class DeviceTokenFirebaseCloudMessaging(Object):
    """
    A token for Firebase Cloud Messaging 

    Attributes:
        ID (:obj:`str`): ``DeviceTokenFirebaseCloudMessaging``

    Args:
        token (:obj:`str`):
            Device registration token; may be empty to de-register a device 
        encrypt (:obj:`bool`):
            True, if push notifications should be additionally encrypted

    Returns:
        DeviceToken

    Raises:
        :class:`telegram.Error`
    """
    ID = "deviceTokenFirebaseCloudMessaging"

    def __init__(self, token, encrypt, **kwargs):
        
        self.token = token  # str
        self.encrypt = encrypt  # bool

    @staticmethod
    def read(q: dict, *args) -> "DeviceTokenFirebaseCloudMessaging":
        token = q.get('token')
        encrypt = q.get('encrypt')
        return DeviceTokenFirebaseCloudMessaging(token, encrypt)
