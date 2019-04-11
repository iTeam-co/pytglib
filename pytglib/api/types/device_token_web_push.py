

from ..utils import Object


class DeviceTokenWebPush(Object):
    """
    A token for web Push API 

    Attributes:
        ID (:obj:`str`): ``DeviceTokenWebPush``

    Args:
        endpoint (:obj:`str`):
            Absolute URL exposed by the push service where the application server can send push messages; may be empty to de-register a device
        p256dh_base64url (:obj:`str`):
            Base64url-encoded P-256 elliptic curve Diffie-Hellman public key 
        auth_base64url (:obj:`str`):
            Base64url-encoded authentication secret

    Returns:
        DeviceToken

    Raises:
        :class:`telegram.Error`
    """
    ID = "deviceTokenWebPush"

    def __init__(self, endpoint, p256dh_base64url, auth_base64url, **kwargs):
        
        self.endpoint = endpoint  # str
        self.p256dh_base64url = p256dh_base64url  # str
        self.auth_base64url = auth_base64url  # str

    @staticmethod
    def read(q: dict, *args) -> "DeviceTokenWebPush":
        endpoint = q.get('endpoint')
        p256dh_base64url = q.get('p256dh_base64url')
        auth_base64url = q.get('auth_base64url')
        return DeviceTokenWebPush(endpoint, p256dh_base64url, auth_base64url)
