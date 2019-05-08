

from ..utils import Object


class DeviceToken(Object):
    """
    Represents a data needed to subscribe for push notifications through registerDevice method. To use specific push notification service, you must specify the correct application platform and upload valid server authentication data at https://my.telegram.org

    No parameters required.
    """
    ID = "deviceToken"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "DeviceTokenFirebaseCloudMessaging or DeviceTokenApplePush or DeviceTokenTizenPush or DeviceTokenWebPush or DeviceTokenMicrosoftPushVoIP or DeviceTokenMicrosoftPush or DeviceTokenBlackBerryPush or DeviceTokenApplePushVoIP or DeviceTokenSimplePush or DeviceTokenWindowsPush or DeviceTokenUbuntuPush":
        if q.get("@type"):
            return Object.read(q)
        return DeviceToken()
