

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
    def read(q: dict, *args) -> "UserPrivacySettingRuleRestrictUsers or UserPrivacySettingRuleRestrictContacts or UserPrivacySettingRuleAllowAll or UserPrivacySettingRuleAllowUsers or UserPrivacySettingRuleAllowContacts or UserPrivacySettingRuleRestrictAll":
        if q.get("@type"):
            return Object.read(q)
        return UserPrivacySettingRule()
