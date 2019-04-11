

from ..utils import Object


class UserPrivacySettingRuleRestrictContacts(Object):
    """
    A rule to restrict all contacts of a user from doing something

    Attributes:
        ID (:obj:`str`): ``UserPrivacySettingRuleRestrictContacts``

    No parameters required.

    Returns:
        UserPrivacySettingRule

    Raises:
        :class:`telegram.Error`
    """
    ID = "userPrivacySettingRuleRestrictContacts"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "UserPrivacySettingRuleRestrictContacts":
        
        return UserPrivacySettingRuleRestrictContacts()
