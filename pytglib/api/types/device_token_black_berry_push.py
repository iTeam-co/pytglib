

from ..utils import Object


class DeviceTokenBlackBerryPush(Object):
    """
    A token for BlackBerry Push Service 

    Attributes:
        ID (:obj:`str`): ``DeviceTokenBlackBerryPush``

    Args:
        token (:obj:`str`):
            Token; may be empty to de-register a device

    Returns:
        DeviceToken

    Raises:
        :class:`telegram.Error`
    """
    ID = "deviceTokenBlackBerryPush"

    def __init__(self, token, **kwargs):
        
        self.token = token  # str

    @staticmethod
    def read(q: dict, *args) -> "DeviceTokenBlackBerryPush":
        token = q.get('token')
        return DeviceTokenBlackBerryPush(token)
