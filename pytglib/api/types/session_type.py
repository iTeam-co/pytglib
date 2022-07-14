

from ..utils import Object


class SessionType(Object):
    """
    Represents the type of a session

    No parameters required.
    """
    ID = "sessionType"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SessionTypeUbuntu or SessionTypeVivaldi or SessionTypeApple or SessionTypeBrave or SessionTypeChrome or SessionTypeWindows or SessionTypeXbox or SessionTypeLinux or SessionTypeOpera or SessionTypeFirefox or SessionTypeEdge or SessionTypeAndroid or SessionTypeIpad or SessionTypeIphone or SessionTypeUnknown or SessionTypeSafari or SessionTypeMac":
        if q.get("@type"):
            return Object.read(q)
        return SessionType()
