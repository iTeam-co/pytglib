

from ..utils import Object


class DeviceTokenTizenPush(Object):
    """
    A token for Tizen Push Service 

    Attributes:
        ID (:obj:`str`): ``DeviceTokenTizenPush``

    Args:
        reg_id (:obj:`str`):
            Push service registration identifier; may be empty to de-register a device

    Returns:
        DeviceToken

    Raises:
        :class:`telegram.Error`
    """
    ID = "deviceTokenTizenPush"

    def __init__(self, reg_id, **kwargs):
        
        self.reg_id = reg_id  # str

    @staticmethod
    def read(q: dict, *args) -> "DeviceTokenTizenPush":
        reg_id = q.get('reg_id')
        return DeviceTokenTizenPush(reg_id)
