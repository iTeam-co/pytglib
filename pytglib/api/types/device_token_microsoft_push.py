

from ..utils import Object


class DeviceTokenMicrosoftPush(Object):
    """
    A token for Microsoft Push Notification Service 

    Attributes:
        ID (:obj:`str`): ``DeviceTokenMicrosoftPush``

    Args:
        channel_uri (:obj:`str`):
            Push notification channel URI; may be empty to de-register a device

    Returns:
        DeviceToken

    Raises:
        :class:`telegram.Error`
    """
    ID = "deviceTokenMicrosoftPush"

    def __init__(self, channel_uri, **kwargs):
        
        self.channel_uri = channel_uri  # str

    @staticmethod
    def read(q: dict, *args) -> "DeviceTokenMicrosoftPush":
        channel_uri = q.get('channel_uri')
        return DeviceTokenMicrosoftPush(channel_uri)
