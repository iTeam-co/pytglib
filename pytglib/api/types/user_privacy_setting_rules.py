

from ..utils import Object


class UserPrivacySettingRules(Object):
    """
    A list of privacy rules. Rules are matched in the specified order. The first matched rule defines the privacy setting for a given user. If no rule matches, the action is not allowed 

    Attributes:
        ID (:obj:`str`): ``UserPrivacySettingRules``

    Args:
        rules (List of :class:`telegram.api.types.UserPrivacySettingRule`):
            A list of rules

    Returns:
        UserPrivacySettingRules

    Raises:
        :class:`telegram.Error`
    """
    ID = "userPrivacySettingRules"

    def __init__(self, rules, **kwargs):
        
        self.rules = rules  # list of UserPrivacySettingRule

    @staticmethod
    def read(q: dict, *args) -> "UserPrivacySettingRules":
        rules = [Object.read(i) for i in q.get('rules', [])]
        return UserPrivacySettingRules(rules)
