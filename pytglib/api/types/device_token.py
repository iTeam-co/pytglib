

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
    def read(q: dict, *args) -> "DeviceTokenMicrosoftPushVoIP or DeviceTokenWindowsPush or DeviceTokenBlackBerryPush or DeviceTokenApplePushVoIP or DeviceTokenApplePush or DeviceTokenUbuntuPush or DeviceTokenMicrosoftPush or DeviceTokenFirebaseCloudMessaging or DeviceTokenSimplePush or DeviceTokenWebPush or DeviceTokenTizenPush":
        if q.get("@type"):
            return Object.read(q)
        return DeviceToken()
