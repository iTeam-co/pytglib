

from ..utils import Object


class DeviceToken(Object):
    """
    Represents a data needed to subscribe for push notifications. To use specific push notification service, you must specify the correct application platform and upload valid server authentication data at https://my.telegram.org

    No parameters required.
    """
    ID = "deviceToken"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "DeviceTokenWebPush or DeviceTokenSimplePush or DeviceTokenTizenPush or DeviceTokenWindowsPush or DeviceTokenMicrosoftPush or DeviceTokenApplePushVoIP or DeviceTokenApplePush or DeviceTokenMicrosoftPushVoIP or DeviceTokenUbuntuPush or DeviceTokenBlackBerryPush or DeviceTokenGoogleCloudMessaging":
        if q.get("@type"):
            return Object.read(q)
        return DeviceToken()
