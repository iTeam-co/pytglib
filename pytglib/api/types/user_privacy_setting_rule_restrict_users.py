

from ..utils import Object


class UserPrivacySettingRuleRestrictUsers(Object):
    """
    A rule to restrict all specified users from doing something 

    Attributes:
        ID (:obj:`str`): ``UserPrivacySettingRuleRestrictUsers``

    Args:
        user_ids (List of :obj:`int`):
            The user identifiers, total number of users in all rules must not exceed 1000

    Returns:
        UserPrivacySettingRule

    Raises:
        :class:`telegram.Error`
    """
    ID = "userPrivacySettingRuleRestrictUsers"

    def __init__(self, user_ids, **kwargs):
        
        self.user_ids = user_ids  # list of int

    @staticmethod
    def read(q: dict, *args) -> "UserPrivacySettingRuleRestrictUsers":
        user_ids = q.get('user_ids')
        return UserPrivacySettingRuleRestrictUsers(user_ids)
