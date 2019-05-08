

from ..utils import Object


class UserPrivacySettingAllowPeerToPeerCalls(Object):
    """
    A privacy setting for managing whether peer-to-peer connections can be used for calls

    Attributes:
        ID (:obj:`str`): ``UserPrivacySettingAllowPeerToPeerCalls``

    No parameters required.

    Returns:
        UserPrivacySetting

    Raises:
        :class:`telegram.Error`
    """
    ID = "userPrivacySettingAllowPeerToPeerCalls"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "UserPrivacySettingAllowPeerToPeerCalls":
        
        return UserPrivacySettingAllowPeerToPeerCalls()
