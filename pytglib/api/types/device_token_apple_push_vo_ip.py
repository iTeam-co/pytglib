

from ..utils import Object


class DeviceTokenApplePushVoIP(Object):
    """
    A token for Apple Push Notification service VoIP notifications 

    Attributes:
        ID (:obj:`str`): ``DeviceTokenApplePushVoIP``

    Args:
        device_token (:obj:`str`):
            Device token; may be empty to de-register a device 
        is_app_sandbox (:obj:`bool`):
            True, if App Sandbox is enabled

    Returns:
        DeviceToken

    Raises:
        :class:`telegram.Error`
    """
    ID = "deviceTokenApplePushVoIP"

    def __init__(self, device_token, is_app_sandbox, **kwargs):
        
        self.device_token = device_token  # str
        self.is_app_sandbox = is_app_sandbox  # bool

    @staticmethod
    def read(q: dict, *args) -> "DeviceTokenApplePushVoIP":
        device_token = q.get('device_token')
        is_app_sandbox = q.get('is_app_sandbox')
        return DeviceTokenApplePushVoIP(device_token, is_app_sandbox)
