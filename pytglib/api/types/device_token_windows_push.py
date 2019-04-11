

from ..utils import Object


class DeviceTokenWindowsPush(Object):
    """
    A token for Windows Push Notification Services 

    Attributes:
        ID (:obj:`str`): ``DeviceTokenWindowsPush``

    Args:
        access_token (:obj:`str`):
            The access token that will be used to send notifications; may be empty to de-register a device

    Returns:
        DeviceToken

    Raises:
        :class:`telegram.Error`
    """
    ID = "deviceTokenWindowsPush"

    def __init__(self, access_token, **kwargs):
        
        self.access_token = access_token  # str

    @staticmethod
    def read(q: dict, *args) -> "DeviceTokenWindowsPush":
        access_token = q.get('access_token')
        return DeviceTokenWindowsPush(access_token)
