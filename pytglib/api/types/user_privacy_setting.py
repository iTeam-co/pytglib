

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
    def read(q: dict, *args) -> "UserPrivacySettingAllowPeerToPeerCalls or UserPrivacySettingShowStatus or UserPrivacySettingShowLinkInForwardedMessages or UserPrivacySettingAllowFindingByPhoneNumber or UserPrivacySettingAllowChatInvites or UserPrivacySettingShowPhoneNumber or UserPrivacySettingShowProfilePhoto or UserPrivacySettingAllowCalls":
        if q.get("@type"):
            return Object.read(q)
        return UserPrivacySetting()
