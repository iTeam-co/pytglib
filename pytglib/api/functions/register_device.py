

from ..utils import Object


class RegisterDevice(Object):
    """
    Registers the currently used device for receiving push notifications. Returns a globally unique identifier of the push notification subscription 

    Attributes:
        ID (:obj:`str`): ``RegisterDevice``

    Args:
        device_token (:class:`telegram.api.types.DeviceToken`):
            Device token 
        other_user_ids (List of :obj:`int`):
            List of user identifiers of other users currently using the client

    Returns:
        PushReceiverId

    Raises:
        :class:`telegram.Error`
    """
    ID = "registerDevice"

    def __init__(self, device_token, other_user_ids, extra=None, **kwargs):
        self.extra = extra
        self.device_token = device_token  # DeviceToken
        self.other_user_ids = other_user_ids  # list of int

    @staticmethod
    def read(q: dict, *args) -> "RegisterDevice":
        device_token = Object.read(q.get('device_token'))
        other_user_ids = q.get('other_user_ids')
        return RegisterDevice(device_token, other_user_ids)
