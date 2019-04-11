

from ..utils import Object


class DeviceTokenApplePush(Object):
    """
    A token for Apple Push Notification service 

    Attributes:
        ID (:obj:`str`): ``DeviceTokenApplePush``

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
    ID = "deviceTokenApplePush"

    def __init__(self, device_token, is_app_sandbox, **kwargs):
        
        self.device_token = device_token  # str
        self.is_app_sandbox = is_app_sandbox  # bool

    @staticmethod
    def read(q: dict, *args) -> "DeviceTokenApplePush":
        device_token = q.get('device_token')
        is_app_sandbox = q.get('is_app_sandbox')
        return DeviceTokenApplePush(device_token, is_app_sandbox)
