

from ..utils import Object


class UserPrivacySettingRuleAllowContacts(Object):
    """
    A rule to allow all of a user's contacts to do something

    Attributes:
        ID (:obj:`str`): ``UserPrivacySettingRuleAllowContacts``

    No parameters required.

    Returns:
        UserPrivacySettingRule

    Raises:
        :class:`telegram.Error`
    """
    ID = "userPrivacySettingRuleAllowContacts"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "UserPrivacySettingRuleAllowContacts":
        
        return UserPrivacySettingRuleAllowContacts()
