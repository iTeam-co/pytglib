

from ..utils import Object


class DeviceToken(Object):
    """
    Represents a data needed to subscribe for push notifications through registerDevice method. To use specific push notification service, the correct application platform must be specified and a valid server authentication data must be uploaded at https://my.telegram.org

    No parameters required.
    """
    ID = "deviceToken"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "DeviceTokenUbuntuPush or DeviceTokenTizenPush or DeviceTokenWindowsPush or DeviceTokenSimplePush or DeviceTokenBlackBerryPush or DeviceTokenWebPush or DeviceTokenMicrosoftPush or DeviceTokenMicrosoftPushVoIP or DeviceTokenFirebaseCloudMessaging or DeviceTokenApplePushVoIP or DeviceTokenApplePush":
        if q.get("@type"):
            return Object.read(q)
        return DeviceToken()
