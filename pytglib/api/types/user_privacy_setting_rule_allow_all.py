

from ..utils import Object


class UserPrivacySettingRuleAllowAll(Object):
    """
    A rule to allow all users to do something

    Attributes:
        ID (:obj:`str`): ``UserPrivacySettingRuleAllowAll``

    No parameters required.

    Returns:
        UserPrivacySettingRule

    Raises:
        :class:`telegram.Error`
    """
    ID = "userPrivacySettingRuleAllowAll"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "UserPrivacySettingRuleAllowAll":
        
        return UserPrivacySettingRuleAllowAll()
