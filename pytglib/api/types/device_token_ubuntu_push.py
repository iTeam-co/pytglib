

from ..utils import Object


class DeviceTokenUbuntuPush(Object):
    """
    A token for Ubuntu Push Client service 

    Attributes:
        ID (:obj:`str`): ``DeviceTokenUbuntuPush``

    Args:
        token (:obj:`str`):
            Token; may be empty to de-register a device

    Returns:
        DeviceToken

    Raises:
        :class:`telegram.Error`
    """
    ID = "deviceTokenUbuntuPush"

    def __init__(self, token, **kwargs):
        
        self.token = token  # str

    @staticmethod
    def read(q: dict, *args) -> "DeviceTokenUbuntuPush":
        token = q.get('token')
        return DeviceTokenUbuntuPush(token)
