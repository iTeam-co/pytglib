

from ..utils import Object


class UserPrivacySettingRule(Object):
    """
    Represents a single rule for managing privacy settings

    No parameters required.
    """
    ID = "userPrivacySettingRule"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "UserPrivacySettingRuleAllowUsers or UserPrivacySettingRuleAllowAll or UserPrivacySettingRuleAllowContacts or UserPrivacySettingRuleRestrictContacts or UserPrivacySettingRuleRestrictAll or UserPrivacySettingRuleRestrictUsers":
        if q.get("@type"):
            return Object.read(q)
        return UserPrivacySettingRule()
