

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
    def read(q: dict, *args) -> "UserPrivacySettingRuleAllowContacts or UserPrivacySettingRuleRestrictUsers or UserPrivacySettingRuleAllowAll or UserPrivacySettingRuleRestrictContacts or UserPrivacySettingRuleAllowUsers or UserPrivacySettingRuleRestrictAll":
        if q.get("@type"):
            return Object.read(q)
        return UserPrivacySettingRule()
