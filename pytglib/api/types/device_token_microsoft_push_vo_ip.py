

from ..utils import Object


class DeviceTokenMicrosoftPushVoIP(Object):
    """
    A token for Microsoft Push Notification Service VoIP channel 

    Attributes:
        ID (:obj:`str`): ``DeviceTokenMicrosoftPushVoIP``

    Args:
        channel_uri (:obj:`str`):
            Push notification channel URI; may be empty to de-register a device

    Returns:
        DeviceToken

    Raises:
        :class:`telegram.Error`
    """
    ID = "deviceTokenMicrosoftPushVoIP"

    def __init__(self, channel_uri, **kwargs):
        
        self.channel_uri = channel_uri  # str

    @staticmethod
    def read(q: dict, *args) -> "DeviceTokenMicrosoftPushVoIP":
        channel_uri = q.get('channel_uri')
        return DeviceTokenMicrosoftPushVoIP(channel_uri)
