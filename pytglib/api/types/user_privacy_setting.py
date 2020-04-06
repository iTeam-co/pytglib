

from ..utils import Object


class UserPrivacySetting(Object):
    """
    Describes available user privacy settings

    No parameters required.
    """
    ID = "userPrivacySetting"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "UserPrivacySettingAllowCalls or UserPrivacySettingShowPhoneNumber or UserPrivacySettingAllowPeerToPeerCalls or UserPrivacySettingShowLinkInForwardedMessages or UserPrivacySettingShowStatus or UserPrivacySettingShowProfilePhoto or UserPrivacySettingAllowChatInvites or UserPrivacySettingAllowFindingByPhoneNumber":
        if q.get("@type"):
            return Object.read(q)
        return UserPrivacySetting()
