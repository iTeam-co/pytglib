

from ..utils import Object


class UserPrivacySettingRuleRestrictAll(Object):
    """
    A rule to restrict all users from doing something

    Attributes:
        ID (:obj:`str`): ``UserPrivacySettingRuleRestrictAll``

    No parameters required.

    Returns:
        UserPrivacySettingRule

    Raises:
        :class:`telegram.Error`
    """
    ID = "userPrivacySettingRuleRestrictAll"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "UserPrivacySettingRuleRestrictAll":
        
        return UserPrivacySettingRuleRestrictAll()
