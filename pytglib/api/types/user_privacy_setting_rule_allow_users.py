

from ..utils import Object


class UserPrivacySettingRuleAllowUsers(Object):
    """
    A rule to allow certain specified users to do something 

    Attributes:
        ID (:obj:`str`): ``UserPrivacySettingRuleAllowUsers``

    Args:
        user_ids (List of :obj:`int`):
            The user identifiers, total number of users in all rules must not exceed 1000

    Returns:
        UserPrivacySettingRule

    Raises:
        :class:`telegram.Error`
    """
    ID = "userPrivacySettingRuleAllowUsers"

    def __init__(self, user_ids, **kwargs):
        
        self.user_ids = user_ids  # list of int

    @staticmethod
    def read(q: dict, *args) -> "UserPrivacySettingRuleAllowUsers":
        user_ids = q.get('user_ids')
        return UserPrivacySettingRuleAllowUsers(user_ids)
